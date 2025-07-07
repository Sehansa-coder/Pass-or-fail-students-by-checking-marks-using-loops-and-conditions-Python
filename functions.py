def my_function():
    a=2
    b=3
    c=a+b
    print(c)
    return c
my_function()

# another way
def addition(x:int,y:int):
    sum=x+y
    return sum
result=addition(10,20)
print(result)

# using strings
def greeting(name:str):
    print("Hello",name)
greeting(" Sehansa")
greeting(" Dewlini")

# functions with default parameters

def lets_add(num1:int,num2=10):
    tot=num1+num2
    return tot
answer=lets_add(20)
print(answer)





