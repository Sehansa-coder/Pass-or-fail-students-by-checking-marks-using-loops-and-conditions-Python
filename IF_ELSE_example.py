should_continue=True
while should_continue==True:
    user_input=input("Enter the mark of the student:")

    marks=float(user_input)
    print(marks)
    if marks>=80:
        print("A")
    elif marks>=70: 
        print("B")
    elif marks>=60:
        print("C")
    elif marks>=50:
        print("D")
    elif marks>=40:
        print("E")
    else:
        print("F")


    answer=input("Do you want to continut? (yes/no):")   # use to iterate or exit from the loop
    if answer=='no':
        break
    else:
        continue
print('Thak you')







 
