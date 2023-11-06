N = int(input("Enter the count of numbers: "))
sum_odd = 0
sum_even = 0
for i in range(N):
      num = int(input("Enter the num: "))
      if num %2!= 0:
          sum_odd=sum_odd+num
      else:
          sum_even=sum_even+num

print('the sum of even numbers=',sum_even)
print('the sum of odd numbers',sum_odd)
