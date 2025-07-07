students=1
total=0
while students<=5:
    user_input=input("Enter the mark of the student:")
    marks=float(user_input)
    print(marks)
    if marks<40:
        print("F")
    elif marks<70:
        print("C")
    elif marks<=100 and marks>=70:    # we put the condition that the mark should have a limit upto 100
        print("A")
    else:
        print("Error")
    
    # increment the number of students
    students+=1 
    # get the total of 5 students' marks     
    total+=marks     

print(total)
average=total/students
print(average)
print("Thank you")


