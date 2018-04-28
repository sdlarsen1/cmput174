#Lab 8
#reads unspecified string of integers, finds occurance of each number

def histogram(lst):
    d = {}
    for x in lst:
        if x not in d:
            d[x] = 1
        else:
            d[x] = d[x] + 1
    return d

def printfunction(dictionary):
    for x in dictionary:
        if dictionary[x] == 1:
            print(x+" occurs one time")
        else:
            print(x+" occurs "+str(dictionary[x])+" times")

def main():
    numbers = input("Enter numbers seperated by spaces >")
    numbers = numbers.split()
    print(histogram(numbers))
    printfunction(histogram(numbers))
main()