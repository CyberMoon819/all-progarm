'''import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(t

try:
  f = open("hello.txt")
  try:
    f.read("hi")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  

import numpy
arr = numpy.array([1,2,3,4,5])
print(arr)

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()

input_str = 'Kumar_Ravi_003'
a = input_str.split('_')
first_name = a[1]
second_name = a[0]
customer_code = a[2]
print(first_name +"\n"+ second_name +"\n"+ customer_code)

input_list = ['SAS', 'R', 'PYTHON', 'SPSS'] 
print(input_list)

input_list.remove('SPSS')

input_list.append('SPARK')
print(input_list)

input_str = 'I love Data Science & Python' 
a = input_str.split('&')
print(a)

input_str = ['Pythons syntax is easy to learn', 'Pythons syntax is very clear']
a = " & "
x = a.join(input_str)
print(x)

input_list = [['SAS','R'],['Tableau','SQL'],['Python','Java']]

print(input_list[-1][-2])
'''
t=int(input())

for i in range(t):
  n = int(input())
  if n%3==1:
    print("beautiful")
  elif n%3==2:
    print("pretty")
  elif n%3==0:
    print("good")