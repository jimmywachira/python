class Student:
    def __init__(self,name,house):
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

class Teacher(Student):
    def __init__(self, name, house, subject): 
       super().__init__(name, house)
       self.subject = subject

    def __str__(self):
        return f"{self.name} teaches : {self.subject} and the fee is {Teacher.fee()}"
    
    def fee():
       return f"{Student.get} 500 usd" 
    
        
def main():
    #return Teacher.get()
    return Student.get()

if __name__ == "__main__":
    main()