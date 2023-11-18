def sum(N):
    if N == 1:
        return 1
    else:
        return N**2 + sum(N - 1)
N = int(input("Enter the value of N: "))
result = sum(N)
print("The sum = ",result)