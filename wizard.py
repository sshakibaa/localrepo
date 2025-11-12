# inheritance feature

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name

    def cast_spell(self):
        return f"{self.name} casts a powerful spell!"
    
class Student(Wizard):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def study(self):
        return f"{self.name} is studying magic at {self.school}."
# Example usage
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def teach(self):
        return f"Professor {self.name} is teaching {self.subject}."
    
wizard = Wizard("Gandalf")
student = Student("Harry", "Hogwarts")
professor = Professor("Dumbledore", "Defense Against the Dark Arts")    

# All three can cast spells (inherited method)
#print(wizard.cast_spell())    # "Gandalf casts a powerful spell!"
#print(student.cast_spell())   # "Harry casts a powerful spell!"
#print(professor.cast_spell()) # "Dumbledore casts a powerful spell!"

# Students can study
print(student.study())  # "Harry is studying magic at Hogwarts."

# Professors can teach
print(professor.teach())  # "Professor Dumbledore is teaching Defense Against the Dark Arts."