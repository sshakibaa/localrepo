import sqlite3
from datetime import datetime
from tabulate import tabulate

class FinanceTracker:
    def __init__(self, db_name='finance_tracker.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()
        self.add_default_categories()
    
    def create_tables(self):
        """Create database tables if they don't exist"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                budget_limit REAL,
                type TEXT CHECK(type IN ('income', 'expense'))
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date DATE NOT NULL,
                amount REAL NOT NULL,
                category_id INTEGER,
                description TEXT,
                type TEXT CHECK(type IN ('income', 'expense')),
                FOREIGN KEY (category_id) REFERENCES categories(id)
            )
        ''')
        self.conn.commit()
    
    def add_default_categories(self):
        """Add some default categories if database is empty"""
        self.cursor.execute('SELECT COUNT(*) FROM categories')
        if self.cursor.fetchone()[0] == 0:
            default_categories = [
                ('Salary', None, 'income'),
                ('Freelance', None, 'income'),
                ('Groceries', 500, 'expense'),
                ('Rent', 1000, 'expense'),
                ('Utilities', 200, 'expense'),
                ('Entertainment', 300, 'expense'),
                ('Transportation', 150, 'expense'),
                ('Healthcare', 200, 'expense'),
                ('Other', None, 'expense')
            ]
            self.cursor.executemany(
                'INSERT INTO categories (name, budget_limit, type) VALUES (?, ?, ?)',
                default_categories
            )
            self.conn.commit()
    
    def add_transaction(self, date, amount, category_name, description, trans_type):
        """Add a new transaction"""
        # Get category ID
        self.cursor.execute('SELECT id FROM categories WHERE name = ?', (category_name,))
        result = self.cursor.fetchone()
        
        if not result:
            print(f"Category '{category_name}' not found!")
            return False
        
        category_id = result[0]
        
        self.cursor.execute('''
            INSERT INTO transactions (date, amount, category_id, description, type)
            VALUES (?, ?, ?, ?, ?)
        ''', (date, amount, category_id, description, trans_type))
        
        self.conn.commit()
        print(f"Transaction added successfully! ID: {self.cursor.lastrowid}")
        return True
    
    def view_transactions(self, limit=10):
        """View recent transactions"""
        self.cursor.execute('''
            SELECT t.id, t.date, t.type, c.name, t.amount, t.description
            FROM transactions t
            JOIN categories c ON t.category_id = c.id
            ORDER BY t.date DESC, t.id DESC
            LIMIT ?
        ''', (limit,))
        
        transactions = self.cursor.fetchall()
        
        if transactions:
            headers = ['ID', 'Date', 'Type', 'Category', 'Amount', 'Description']
            print("\n" + tabulate(transactions, headers=headers, tablefmt='grid'))
        else:
            print("\nNo transactions found!")
    
    def view_categories(self):
        """View all categories with budget limits"""
        self.cursor.execute('''
            SELECT name, type, budget_limit
            FROM categories
            ORDER BY type, name
        ''')
        
        categories = self.cursor.fetchall()
        headers = ['Category', 'Type', 'Budget Limit']
        print("\n" + tabulate(categories, headers=headers, tablefmt='grid'))
    
    def add_category(self, name, budget_limit, cat_type):
        """Add a new category"""
        try:
            self.cursor.execute('''
                INSERT INTO categories (name, budget_limit, type)
                VALUES (?, ?, ?)
            ''', (name, budget_limit, cat_type))
            self.conn.commit()
            print(f"Category '{name}' added successfully!")
            return True
        except sqlite3.IntegrityError:
            print(f"Category '{name}' already exists!")
            return False
    
    def monthly_report(self, year, month):
        """Generate monthly spending report"""
        # Income summary
        self.cursor.execute('''
            SELECT c.name, SUM(t.amount) as total
            FROM transactions t
            JOIN categories c ON t.category_id = c.id
            WHERE t.type = 'income' 
            AND strftime('%Y', t.date) = ? 
            AND strftime('%m', t.date) = ?
            GROUP BY c.name
        ''', (str(year), f'{month:02d}'))
        
        income = self.cursor.fetchall()
        total_income = sum(row[1] for row in income)
        
        # Expense summary with budget comparison
        self.cursor.execute('''
            SELECT c.name, SUM(t.amount) as spent, c.budget_limit,
                   CASE 
                       WHEN c.budget_limit IS NOT NULL THEN 
                           ROUND(((SUM(t.amount) / c.budget_limit) * 100), 2)
                       ELSE NULL
                   END as percentage
            FROM transactions t
            JOIN categories c ON t.category_id = c.id
            WHERE t.type = 'expense' 
            AND strftime('%Y', t.date) = ? 
            AND strftime('%m', t.date) = ?
            GROUP BY c.name
            ORDER BY spent DESC
        ''', (str(year), f'{month:02d}'))
        
        expenses = self.cursor.fetchall()
        total_expenses = sum(row[1] for row in expenses)
        
        print(f"\n{'='*60}")
        print(f"MONTHLY REPORT - {year}-{month:02d}")
        print(f"{'='*60}")
        
        print("\n--- INCOME ---")
        if income:
            print(tabulate(income, headers=['Category', 'Amount'], tablefmt='grid'))
        print(f"Total Income: ${total_income:.2f}")
        
        print("\n--- EXPENSES ---")
        if expenses:
            headers = ['Category', 'Spent', 'Budget', '% of Budget']
            print(tabulate(expenses, headers=headers, tablefmt='grid'))
        print(f"Total Expenses: ${total_expenses:.2f}")
        
        print(f"\n--- SUMMARY ---")
        savings = total_income - total_expenses
        print(f"Net Savings: ${savings:.2f}")
        if total_income > 0:
            savings_rate = (savings / total_income) * 100
            print(f"Savings Rate: {savings_rate:.2f}%")
    
    def delete_transaction(self, transaction_id):
        """Delete a transaction by ID"""
        self.cursor.execute('DELETE FROM transactions WHERE id = ?', (transaction_id,))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            print(f"Transaction {transaction_id} deleted successfully!")
            return True
        else:
            print(f"Transaction {transaction_id} not found!")
            return False
    
    def close(self):
        """Close database connection"""
        self.conn.close()


def main():
    tracker = FinanceTracker()
    
    while True:
        print("\n" + "="*50)
        print("PERSONAL FINANCE TRACKER")
        print("="*50)
        print("1. Add Transaction")
        print("2. View Recent Transactions")
        print("3. Add Category")
        print("4. View Categories")
        print("5. Monthly Report")
        print("6. Delete Transaction")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            print("\n--- Add Transaction ---")
            trans_type = input("Type (income/expense): ").lower()
            if trans_type not in ['income', 'expense']:
                print("Invalid type! Use 'income' or 'expense'")
                continue
            
            date = input("Date (YYYY-MM-DD) or press Enter for today: ")
            if not date:
                date = datetime.now().strftime('%Y-%m-%d')
            
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("Invalid amount!")
                continue
            
            tracker.view_categories()
            category = input("Category name: ")
            description = input("Description: ")
            
            tracker.add_transaction(date, amount, category, description, trans_type)
        
        elif choice == '2':
            limit = input("How many transactions to show? (default 10): ")
            limit = int(limit) if limit else 10
            tracker.view_transactions(limit)
        
        elif choice == '3':
            print("\n--- Add Category ---")
            name = input("Category name: ")
            cat_type = input("Type (income/expense): ").lower()
            if cat_type not in ['income', 'expense']:
                print("Invalid type!")
                continue
            
            budget = input("Budget limit (leave empty for no limit): ")
            budget_limit = float(budget) if budget else None
            
            tracker.add_category(name, budget_limit, cat_type)
        
        elif choice == '4':
            tracker.view_categories()
        
        elif choice == '5':
            year = int(input("Year (e.g., 2024): "))
            month = int(input("Month (1-12): "))
            tracker.monthly_report(year, month)
        
        elif choice == '6':
            tracker.view_transactions()
            trans_id = int(input("\nEnter transaction ID to delete: "))
            tracker.delete_transaction(trans_id)
        
        elif choice == '7':
            print("\nThank you for using Finance Tracker!")
            tracker.close()
            break
        
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()