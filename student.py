"""
with open("student.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        print(f"{name} live in {house}")

"""
"""
students = []
with open("student.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        student = {"name": name , "house": house} #create dictonary, in this dict here two key.
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key = get_name,reverse = False): #key is a function 
    #another way for student in sorted(students, key = lambda student: studen['name'],reverse = False):
    print(f"{student['name']} live in {student['house']}")

"""

import csv

students = []
with open("student.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "house":row["house"]})

for student in sorted(students, key = lambda student: student['name']):
    print(f"{student['name']} live in {student['house']}")