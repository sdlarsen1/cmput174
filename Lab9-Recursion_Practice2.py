def gauss(N):
    if N == 1:
        return 1
    else:
        return N + gauss(N-1)

print(gauss(100))