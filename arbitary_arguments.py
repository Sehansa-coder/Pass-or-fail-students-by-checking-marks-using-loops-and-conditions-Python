# we use '*' to show that there can be many arguments

def adding_numbers(*numbers:int):
    tot=0
    for num in numbers:
        tot+=num
    return tot
answer=adding_numbers(1,2,3,4)
print(answer)