def sumlist(L):
    if not L:  # empty list
        return 0
    else:
        return L[0] + sumlist(L[1:])
my_list = [int(x) for x in input("Enter the elements of the list separated by spaces: ").split()]
result = sumlist(my_list)
print(f"The sum of the list is: {result}")