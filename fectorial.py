#recursion in python
def main():
    num = int(input("Enter a number to compute its factorial: "))
    result = factorial(num)
    print(f"The factorial of {num} is {result}")    
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
if __name__ == "__main__":
    main()