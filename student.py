class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        if house not in ['c','d','e','f']:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name : ")
    house = input("House : ")
    return Student(name,house)

#setter
@house.setter
def house(self):
    if self.house not in ['c','d','e','f']:
        raise ValueError("Invalid house")
    return self._house = house

#getter
@property
def house(self,house):
    return self._house

if __name__ == "__main__":
    main()