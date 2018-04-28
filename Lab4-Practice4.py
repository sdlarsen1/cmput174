gradelist=[]
grade=float(input("Enter first grade >"))
gradelist.append(grade)
answer=input("Are there more grades? (Y/N)").upper()

while answer=='Y':
    grade=float(input("Enter first grade >"))
    gradelist.append(grade)
    answer=input("Are there more grades? (Y/N)").upper()

average=sum(gradelist)/len(gradelist)
print("Grades below average:")
for grade in gradelist:
    if grade<average:
        print(grade)
        
'''''''''''
slice operator:
alist=[2,3,4,5,6]
       0,1,2,3,4
alist[:3] (start-->end-1 or 0-2)
[2,3,4]
'''''''''''