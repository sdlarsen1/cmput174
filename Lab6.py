#Lab 6
#Removes duplicates from input string of integers

def eliminateDuplicates(lst):
    checked = []
    for x in lst:
        if x not in checked:
            checked.append(x)
    return checked
        
       
def main():
    numberslist = []
    numbers = input("Enter numbers: ")
    numbers = numbers.split()
    for number in numbers:
        number = int(number)
        numberslist.append(number)
    result = eliminateDuplicates(numberslist)    
    print("The distinct numbers are:",result)
main()