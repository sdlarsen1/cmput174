#Stephen Larsen, 1407008
#Lec B1
#Lab H02
#Finds the hypotenuse, perimeter, and area of a triangle

#Input
import math
sideA=float(input("Enter the length of one side:"))
sideB=float(input("Enter the length of the other side:"))

#Calculate hypotenuse
sideC=math.sqrt((sideA**2)+(sideB**2))

#Calculate area
area=(sideA*sideB)/2

#Calculate perimeter
per=sideA+sideB+sideC

#Output
print("The Hypotenuse is %.2f" %sideC)
print("The area is %.2f" %area)
print("The perimeter is %.2f" %per)