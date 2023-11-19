def count_items(L):
    if not L:  # empty list
        return 0
    else:
        return 1 + count_items(L[1:])
my_list = [int(x) for x in input("Enter the elements of the list separated by spaces: ").split()]
result = count_items(my_list)
print(f"The number of items in the list is: {result}")