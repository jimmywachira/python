class BankAcc:
    def __init__(self,acc_name,bal):
        self.acc_name = acc_name
        self.bal = bal

    def depo (self, amount):
        self.bal = self.bal + amount  
        print(f"{amount} : deposited")
    
    def __str__(self):
        return f"acc holder name: {self.acc_name} \nacc bal: {self.bal}"

    def withdral(self, amount):
        if(amount > self.bal):
            print("insuffcient funds in bank acc")
        else:
            self.bal- amount
            print("successfully withdrew")

bankAcc1 = BankAcc("jimmy",1500)
print(bankAcc1)
bankAcc1.depo(800)
bankAcc1.withdral(15800)
print(bankAcc1)


"""
    class prints area n circ of a circle 
    attributes = pi = 3.142, radius 
    methods = area, circmfrence (piR2 and 2piR)
    returns = area, circumfrence

class Calc:
    pi=3.142

    def __init__(self,radius):
        self.radius= radius

    def get_area(self):
        return self.pi *self.radius *self.radius
    
    def get_circ(self):
        return 2 * self.pi * (self.radius *2)
    
circle1 = Calc(4)
print(f"the area is : {circle1.get_area()}")
circle2 = Calc(2)
print(f"the circumfrence is :  {circle2.get_circ()}")
"""

"""
class Instructor:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.followers = 0
       
    #
    def update_followers(self, follower_name):
        self.followers +=1
        return print(f"i have a new follower called:{follower_name} : {self.followers} followers")

    def display(self,subject_name):
        return print(f"hi, i am {self.name} and i teach {subject_name}")

instructor1 = Instructor("jimmy", "kasarani")
print(instructor1.name)
instructor1.display("python")
instructor1.update_followers("jimmy")
"""