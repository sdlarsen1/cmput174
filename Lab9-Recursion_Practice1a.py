def factorial(n):
    total = 1
    i = 1
    while i <= n:
        total = total * i
        i = i+1
    return total
def main():
    print(factorial(10))
main()