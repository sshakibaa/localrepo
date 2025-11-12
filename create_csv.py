import csv
name = input("what's your name? ")
house = input("what's your house? ")


with open("student.csv","a", newline='') as file:
    #writer = csv.writer(file)
    writer = csv.DictWriter(file, fieldnames= ["name","house"])
    
    #writer.writerow([name,house])

    writer.writerow({"name": name, "house": house})

