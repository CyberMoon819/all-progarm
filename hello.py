'''print("hello")

str1 = "I am"

str2 = " Manoj"

print(str1 + str2)
 
int1 = 22

print(str1 + str(int1))
result = "{1} {0} {2}".format(str1, str2, int1)
print(result)

fstring = f"{str1}{str2}{int1}"
print(fstring)

str1 = "my name is "
str2 = "my dob is "
str3 = "manoj "
str4 = "23.10.2000 "
result = f"{str1}{str3}{str2}{str4}"
print(result)

str1 = "what is ur name?\n"
name = input(str1)
print(f"hello {name} ", end="")
print("nice to meet you")

num1 = input("1st num")
num2 = input("2nd num")

print(f"sum of {num1} and {num2} is {int(num1) + int(num2)}")

mygrocary = ["banana", "guava", "phone", "pen", 90, 78, 79]
print(mygrocary)

mygrocary[0]= "apple"
print(mygrocary)

mygrocary.append("cheez")
print(mygrocary)

mygrocary.insert(1, 1000)
print(mygrocary)

mygrocary.remove("pen")
print(mygrocary)

mygrocary.pop(2)
print(mygrocary)

del mygrocary
print(mygrocary)

mycars = ("ford", "merceded", "audi")
print(mycars[0])

mycarstemp = list(mycars)
print(mycarstemp)

mycarstemp[0] = "harly"
mycars = tuple(mycarstemp)
print(mycars)

dic1 = {
    "name": "manoj",
    "profession": "student",
    "fav movie": "marvel",
    "l": [2,5,4]
}
print(dic1["l"])

print(dic1.get("profession"))

a = dic1.keys()
print(a)

b = dic1.values()
print(b)

c = dic1.items()
print(c)

dic1.pop("l")
print(dic1)

dic1["item"] = "added"
print(dic1)

dic1.clear()
print(dic1)

myset = {1,2,9,5,4,9}
print(myset)

myset.add(56)
myset.update([45, 67])
myset.remove(2)
print(myset)

myset.discard(2)
myset.discard(45)
print(myset)


age = int(input("enter age"))
print(f"you age is {age}")
name = input("enter name")
if age>18 and name != "harry":
    print("you can drive")
#elif age==17:
#    print("magic")
#elif age==45:
#    print("super")
else:
    print("you can't drive"
    
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if num1+num2>100:
    print("numbers are huge")
else:
    print("no problem")

for i in range(100):
    print(i)

mylist = ["this", "that", "harry", "kalita", 45]
for item in mylist:
    print(item)

mytuple =(1,2,3,4,5, "manoj")
for item in mytuple:
    print(item)

mydict = {
    "name": "manoj",
    "color": "black",
    "marks": 100
}
for key, value in mydict.items():
    print(f"the key is {key} and the values is {value}")

Resuls = {
    "Arup": 95,
    "Manoj": 98,
    "Hashim": 99,
    "Rohit": 98,
    "Pranab": 97,
    "Jeevan": 96,
}

for key, value in Resuls.items():
    print(f"The student named '{key}' get {value} marks.")

v=3
r=50
while r>v:
    print(f"the value of r is {r} and the value of v is {v}")
    v=v+10

a=0
while a<7:
    print(a)
    a += 1

name = input("Enter ur name: ")
print(f"ur name is {name.capitalize()}")
print(f"ur name is {name[0].upper() + name[1:]}")

def greet(name):
    print(f"Hey good morning, {name.capitalize()}")
    return 0

name = "manoj"
name1 = "moon"
name2 = "neon"

g = greet(name)
g1 = greet(name1)
g2 = greet(name2)

def add(num1, num2=6):
    result = num1 + num2
    return result

a = 45
b = 55
c = add(a)
print(c)

def mean(num1, num2):
    result = (num1+num2)/2
    return result
a = int(input("a= "))
b = int(input("b= "))
c = mean(a, b)
print(c)
print(c)

numberofline = int(input("enter number of lines: "))
for i in range(numberofline):
    print("*" * (i+1))
    
def printstar(num):
    for i in range(1, num+1):
        print("*" * i)
numodline = int(input("enter number of line: "))

printstar(numodline)

def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)
a=factorial(int(input("enter num: ")))
print(a)
'''
