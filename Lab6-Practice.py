i=0
alist=[]
while i<=2:
    info=input("Enter name of student followed by grade >")
    name,grade=info.split()
    record=(name,float(grade))
    alist.append(record)
    i=i+1
print(alist)

for record in alist:
    print(record[0])