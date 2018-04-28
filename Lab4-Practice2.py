grade_list=[]
grade=int(input("Enter grade >"))
if grade!=0:
    grade_list.append(grade)

while grade!=0:
    grade=int(input("Enter grade >"))
    if grade !=0:
        grade_list.append(grade)

print(grade_list)

maximum=0
for grade in grade_list:#Finding maximum in a list of elements
    if grade>maximum:
        maximum=grade
        print(maximum)#Doesn't work