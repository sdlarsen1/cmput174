#Lab 5
#Converts temps from Farenheit to Celcius using def()

def celciusTemp(F):
    C = (F-32)*5/9
    return C

def main():
    Farenheit = float(input("Enter a temperature in Farenheit: "))
    result = celciusTemp(Farenheit)
    print("The temperaure in Celcius is %.2f" %result)

main()