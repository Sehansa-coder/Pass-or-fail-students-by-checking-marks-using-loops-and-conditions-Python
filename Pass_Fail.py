students=1
count=0
while students<=5:
    user_input=input("Enter your mark:")
    mark=float(user_input)

    if mark<=100 and mark>=0:
        if mark>=50:
            print('Pass')
            count+=1
        else:
            print('Fail')
    else:
        print('Error')
    students+=1
print("Total number of students who has obtained more than 50 marks is=",count)