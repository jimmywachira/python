class Instructor:
    def __init__(self,instructor_name,address):
        self.name = instructor_name
        self.address = address
        
instructor_1 = Instructor("jimmy", "kasarani")
print(instructor_1.name)

"""
import csv

name = input("whats your name ? ")
house = input("whats your house no : ? ")

with open("houses.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","house"])
    writer.writerow({"name":name, "house":house})



import csv

name = input("whats your name ? ")
house = input("whats your house ? ")

with open("houses.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, house])


import csv

students = []

with open("names.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"],"home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")




import csv

students = []

with open("names.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0],"home": row[1]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")



students = []

with open("names.csv") as file:
 for line in file:
  name,house = line.rstrip().split(",")
  student ={"name": name,"house":house}
  students.append(student)

for student in students:
 print(f"{student['name']} is in {student['house']}")

 

with open("names.txt" , "r") as file:
    lines = file.readlines()

for line in lines:
    print(f"hello, {line.rstrip()}") 

name = input("whats your name ? ")
#with open("names.txt", "a") as file:
#    file.write(f"{name}\n")
    
#file = open("names.txt", "a")
#file.write(f"{name}\n")
#file.close()

#sys.exit()
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, ", sys.argv[1])

import random

x = random.randint(1,10)

if x==9:
    print("player one wins")
else:
    print("player two wins")


def main():
    x = get_int()
    print(f"x is : {x}")

def get_int():
    while True:
        try:
            x = int(input("enter an integer x : "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x

main()

def main():
    x=int(input('enter a no : '))
    print_square(x)

def print_square(x):
    for _ in range(x):
        for _ in range(x):
            print("#", end="")
        print()

main()

while True:
    n= int(input("whats n? "))
    if n>0:
        break
for _ in range(n):
    print("meow")


name = int(input('enter house no '))

match name:
    case 1:
        print("kevin")
    case 2|5:
        print("abu or sam")
    case 3:
        print("jimmy")    
    case 4 :
        print("shie")  
    case _:
        print("who")

#parity % modulass to implement even/odd checks
def main():
    x = int(input("enter no:"))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    return n%2==0
    #return True if n%2==0 else False
    if n%2==0:
        return True
    else:
        return False           
main()


def main():
 #ask for input x and y (int's)
 x = int(input("whats the value of x?"))
 y = int(input("whats the value of y?"))

 print("the sum of x and y is:", sum(x,y))
 print(f"{x} squared is:", square(x))
 
#fxn to print the sum
def sum(x,y):
 return x+y

def square(x):
 return pow(x,2)

main()

def main():
    name = input("whats your name? ")
    greet("jimmy")

def greet(jina="guest"):
 print(f"hello, {jina}")
 
main()
"""