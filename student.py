class Student:
    def __init__(self,name,house="c"):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from house : {self.house}"
    

    @classmethod
    def get(cls):
        name = input("Name : ")
        house = input("House : ")
        return cls(name,house)
    
    #getter
    @property
    def name(self):
        return self._name


    #setter
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    #getter
    @property
    def house(self):
        return self._house

    #setter
    @house.setter
    def house(self,house):
        if house not in ['c','d','e','f']:
            raise ValueError("Invalid house")
        self._house = house

#inheritance
class Teacher(Student):
    def __init__(self, name, subject): 
       super().__init__(name)
       self.subject = subject

    def __str__(self):
        return f"{self.name} teaches : {self.subject}"
    
    #def fee():
       #return f"{Student.get()} 500 usd" 
    
        
def main():
    teacher = Teacher('jimmy', 'python')
    return print(teacher)

if __name__ == "__main__":
    main()