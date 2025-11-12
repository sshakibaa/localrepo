#calculate the avg of student marks using oop

import statistics
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        if not self.marks:
            return 0
        return statistics.mean(self.marks)
s1 = Student("Alice", [85, 90, 78, 92])
s2 = Student("Bob", [88, 76, 95, 89])
print(f"{s1.name}'s average marks: {s1.average()}")
print(f"{s2.name}'s average marks: {s2.average()}")