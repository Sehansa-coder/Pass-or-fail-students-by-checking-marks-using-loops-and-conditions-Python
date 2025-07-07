turns=1
while turns<=5:
    user_input=input("Enter the number:")
    num=int(user_input)

    remainder=num%2
    if remainder==0:
        print('Even')
    else:
        print("Odd")
    
    turns+=1