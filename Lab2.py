#Stephen Larsen, 1407008
#Lec B1
#Lab H02
#Takes input score and maximum score values, assigns letter grade

#Input
score=float(input("Please enter the exam score:"))
maximum=float(input("Please enter the maximum score:"))

if maximum<score:#check
    print("Error - student score should be less than maximum score")
else:
    mark=round((score/maximum)*100)#output

    if mark<50:
        print("The percentage is",mark,"and the letter grade is F")

    elif mark<60:
        print("The percentage is",mark,"and the letter grade is D")

    elif mark<75:
        print("The percentage is",mark,"and the letter grade is C")

    elif mark<90:    
        print("The percentage is",mark,"and the letter grade is B")

    else:
        print("The percentage is",mark,"and the letter grade is A")
    