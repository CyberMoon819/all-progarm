'''import math
a = 4.5
print(math.floor(a))
print(math.ceil(a))
print(math.factorial(5))

brands = ["apple", "microsoft", "hp", "dell", "lenovo"]

for item in brands:
    print(f"the name of this brand is {item}")
    if item == "hp":
        break
else:
    print("this is for loop")
 

a = 5
b = int(input("enter b\n"))

c = a+b

serverData = False

try:
    if (serverData):
        d = 6
    print(d)
except Exception as e:
    print(f"it fail because of {e}")

a = int(input("enter a: "))
b = int(input("enter b: "))

c = a-b if a>b else b-a
print(f"the differance between {a} and {b} is {int(c)}")

print("Hello\t \\what\"s \nup")

f = open('hello.txt')  #create file pointer
content = f.read()  #read the file
print(content) #print the content the file
f.close()

f = open('hello.txt', 'w') #write mode 'w' clear the content anf write new content to the file
f = open('hello.txt', 'a') #append mode 'a' add content at the end
f = open('hello.txt', 'at')#if we add t or b to the end, we can specify wheater we want to open the file as a text file or binary file.
f.write("this is done\n")
f.close() 
#create mode 'x' create file and return error if that file already exists

f = open('hello.txt')
content = f.read(2)
print(content)
content = f.read(3)
print(content)

f = open('hello.txt')
line = f.readline()
print(line)
line = f.readline()
print(line)
f.close()

f = open('hello.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
'''