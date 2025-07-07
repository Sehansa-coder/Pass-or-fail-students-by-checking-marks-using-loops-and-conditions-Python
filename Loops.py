#while loop
x=1
while(x<10):
    print(x)
    x+=1

# for loop
numbers=[1,2,3,4,5]
for num in numbers:
    print(num)

# Range function
for i in range(10):
    print(i)

# range ith start and end
for x in range(10,30):
    print(x)

# range with start,end,step
for z in range(10,20,4):
    print(z)
    
# break function in loops
for x in range(1,100):
    if x==50:
        break
    print(x)

# continue function

for c in range(1,100):
    if c==40:
        continue
    print(c)              # 40 will not be printed


# nested loops 

total=0
list=[[1,2,3],[4,5,6],[7,8,9]]
for row in list:
    for num in row:
        total+=num
        print(total)