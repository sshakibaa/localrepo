# oop learning


class Student:
    def __init__(self, name, house):

        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["mirpur", "uttara", "tongi"]:
            raise ValueError("Invalid House")
        self._house = house

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name,house)

def main():
    student = Student.get()
    # print(f"{student.name} from {student.house}")
    print(student)


"""def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
"""

if __name__ == "__main__":
    main()
