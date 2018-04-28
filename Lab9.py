def harmonic(n):
    if n == 1:
        return 1
    else:
        return (1/n) + (harmonic(n-1))
def main():
    number = int(input("Please enter a number >"))
    print("Result = %.2f" %harmonic(number))
main()