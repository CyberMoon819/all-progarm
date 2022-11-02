'''actual_number = 45
guess_number = int(input("Guess a number: "))

if guess_number < actual_number:
        print("laser than actual number")
elif guess_number> actual_number:
    print("greater than actual number ")
else:
    print("you guess the number")

actual_number = 45
attempts = 0

while True:
    attempts += 1
    guess = int(input("Guess the number: "))
    if guess<actual_number:
        print("your guess was too low")
    elif guess>actual_number:
        print("Your guess was too high")
    else:
        print(f"Your guessed the number in {attempts} attempts")
        break
print("Thanks for guessing")

myFood = ['apple', 34, 'orange', 'watermalon', 98, 57]

nonInt = []
#without list comprehension
for item in myFood:
    if not str(item).isdigit():
        nonInt.append(item)
print(nonInt)
#using list comprehension
nonInt2 = [item for item in myFood if str(item).isdigit()]
print(nonInt2)


def harry():
    list1 = []
    for i in range(1000):
        list1.append(i)
    return list1
a = harry()

def manoj():
    for i in range(3):
        yield i
a = manoj()
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

name = "harry"
itretor = name.__iter__()
print(itretor.__next__())
print(itretor.__next__())
print(itretor.__next__())
print(itretor.__next__())
print(itretor.__next__())
print(itretor.__next__())

def printn(string, n):
    for i in range(n):
        print(string)
printn("Manoj", 5)

multiply = lambda a, b: a*b
c = multiply(5, 4)
print(c)
'''
