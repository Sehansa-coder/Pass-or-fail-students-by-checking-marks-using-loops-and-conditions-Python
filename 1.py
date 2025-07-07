x=64
print(x)
print(type(x))
y=0b1000000
print(y)

a=12.5678
b=12.5678e2
print(b)  # e means base 10 and 2 is index- 10^2
print(type(a))

#boolean
c=1
d=2
print(c>d)
print(c==d)
name='sehansa'
print(type(name))
print(name.upper())
print(name[0])

colours=["red","yellow","blue"]
print(type(colours))
colours.append("green")
print(colours)

# converts float to int
e=10.5
print(int(e))           
print(e+2)

#conditional statements
g=1
h=2
if g==1:
  print('you are odd')
else:
  print('you are even')

if g==1 or h==3:
  print('ok')
else:
  print('not ok')

# more if statements
if g==5:
  print('A')
elif g==3:
  print('B')
else:
  print('C')


# case statement(match)

mark=20
match mark:
  case 5:
    print("A")
  case 10:
    print("B")
  case 15:
    print("C")
  case 20:
    print("D")

# Branch prediction 

# While loop

count=1
while count<=5:
  print("Hello")
  count=count+1

# For loop

numbers=[1,2,3,4]
for num in numbers:
  print(num)
names=["Sehansa","Dewlini","Rushna"]
for i in names:
  print(i)

# Range function
# used in sequencial data

for x in range(10):
  print(x)
print("doneeeeeeeee")

# using range with format - range(start,end)
for x in range(1,5):
  print(x)

# using range with format - range(start,end,step)
print("done")
for x in range(0,10,2):
  print(x)

# Break function

for x in range(1,1000):
  if x==555:
    break
  print(x)

# Continue function

for x in range(0,10):
  if x==5:
    continue       # 5 is not printed because if condition checks whether equals to 5 and iterate to continue
  print(x)

# nested loop

total=0
list=[[1,2,3],[4,5,6],[7,8,9]]
for row in list:
  
  for element in row:
    total=total+element

print(total)


# Functions

def my_name():
  print("Sehansa")

my_name()

def add_numbers(a:int,b:int):
  total=a+b
  return total
result=add_numbers(2,10)
print(result)

def greeting(name: str):
  print("Hello",name)
greeting("Sehansa")
greeting("Dewlini")

# Can use many arguments in parameters()

# Function with default parameters(default arguments)

def add_numbers(num1,num2=10):
  total=num1+num2
  return total
answer=add_numbers(2)
print(answer)

# keyword arguments
def multiply_numbers(no1,no2):
  sum=no1*no2
  return sum
ans=multiply_numbers(no1=10,no2=10)
print(ans)

# Arbitary arguments

def adding_many_numbers(*numbers:int):       # * means there can be many arguments
  tot=0
  for num in numbers:
    
    tot=tot+num
  return tot
print(adding_many_numbers(1,2,3,4))

# Arbitary keyword arguments

def person(name:str,**details):
  print("Name is=",name)
  print(details)
person("sehansa",age=18,city="colombo")

# two ** means that there can be many keywords 



# Fibbonacci series

def no(n):
  if n<=1:
    return n
  else:
    return no(n-1)+no(n-2)
for i in range(10):
  print(no(i))

# constant values are better to write in capital
PI=3.14


print("enclosing scope")
#enclosing scope

def total(n1,n2):
  total_val=0

  def calc_total(x,y):
    nonlocal total_val      
    total_val=x+y
  
  calc_total(n1,n2)
  return total_val

result=total(10,20)
print(result)

# nonlocal should define cuz if not total_value will be loccal variable to calc_total function.

# global scope

def add_numbers(n1,n2):
  global sum
  sum=n1+n2
  return sum
  
add_numbers(70,20)
print(sum)

# global sum is used cuz it should be able to use out of the function anywhere-in printing part 
#                                            cannot use the sum without declaring as global sum




tot_value=0
def total(n1,n2):  
  tot_value=n1+n2
total(10,20)
print(tot_value)

# the above code will give 0 cuz tot_value is defined in a function as (tot_value=n1+n2)
#correct code is below

tot_value=0
def total(n1,n2):
  global tot_value
  tot_value=n1+n2
total(11,11)
print(tot_value)


#scope hierachy
x=10
def my_function():
  x=20
  print("my_function x is =",x)

  def my_inner_function():
    x=30
    print("my_inner_function x is =",x)

  my_inner_function()

my_function()
print("global x is =",x)

# accoeding to the hierachy if we remove x=30, it looks for x in outer scope
x=10
def my_function():
  x=20
  print("my_function x is =",x)

  def my_inner_function():
    print("my_inner_function x is =",x)

  my_inner_function()

my_function()
print("global x is =",x)


# import module to another place and accessing it
import module_import
x=6
y=5
tot=module_import.total(x,y)
print(tot)

a=2
b=4
mul=module_import.multiply(a,b)
print(mul)


# using 'alias' to refer a module

import module_import as hehe
x=10
y=50
sum=hehe.total(x,y)
print(sum)

n=80
m=90
cross=hehe.multiply(n,m)
print(cross)


#List

fruits=["apple","banana","orange"]
print(fruits)
print(fruits[0])

fruits.append("mango")
print(fruits)

fruits.insert(2,"grapes")
print(fruits)

#adding multiple elements,so use as a list

fruits.extend(["kiwi","papaw"])
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.pop()    #remove the last element and show/return it
print(fruits)

for item in fruits:
  print(item)

# Tuple
#used to show data that are related to each other
#immutable

person1=("kasun","europe",42,"kasun")
person2=("sadun","srilanka",32)
person3=("nimal","sweden",21)
 
print(person1[0])
print(person2[1])
print(person3[2])

print(person1.count("kasun"))   #print how many times kasun has used in the tuple
print(person2.index("sadun"))


numbers=(1,2,3,4,5,6)
print(2 in numbers)  # check whether 2 is in the tuple
print(5 not in numbers)

numbers1=(1,2)
numbers2=(3,4)
print(numbers1+numbers2)
print(numbers1*2)
print(min(numbers1))
print(max(numbers2))

#slice

food=["rice","sambol","egg","pizza","burger"]
print(food[0:2])

# sets
#cannot have duplicate values,it omit one of it
my_set={1,"seha",2,1}
print(my_set)

#intersection

set1={1,2,3}
set2={4,5,6}

intersection=set1.intersection(set2)
print(intersection) 
# set()

class1={1,2,3,4}
class2={2,4,5,6,7}
common=class1.intersection(class2)
print(common)

#union
all=class1.union(class2)
print(all)

#difference
unique_no_in_class1=class1.difference(class2)
print(unique_no_in_class1)

unique_no_in_class2=class2.difference(class1)
print(unique_no_in_class2)

#dictionary

grocery={"apple":80,
         "banana":30,
         "flour":100
      }
print(grocery["apple"]) # accesing the value of apple
grocery["flour"]=120  # changing the value of flour
print(grocery["flour"])

del grocery["banana"]   # deleting banana from the dictionary
print(grocery)

grocery["orange"]=50   # adding orange to the dictionary
print(grocery)

for product,quantity in grocery.items():
  print(product,"-",quantity)

#using loops above, use variables to access both product and its quantity

#deque

from collections import deque

dq=deque()

dq.append(20)
dq.append(30)

dq.appendleft(5)
dq.pop()
print(dq)   

#remove the last element

dq.popleft()    # remove the first element
print(dq)

from collections import deque

people=deque(maxlen=3)   # limit the length of deque to 3 elements

people.append("catherine")
people.append("jone")
people.append("maria")
people.append("Wick")
people.append("Serina")

for name in people:0
print(name)

#generate random nuumbers

import random

random_number=random.random()
print(random_number)

import math
answer= math.sqrt(4)
print(answer)

#u can refer python standard library to import functions

import datetime
current_date=datetime.datetime.now()
print(current_date)
print(current_date.year)
print(current_date.month)

