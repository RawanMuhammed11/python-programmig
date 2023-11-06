statement = input("Enter a statement: ").lower()
vowels = ['a', 'e', 'i', 'o', 'u']
count_vowels = 0

for letter in statement:
    if letter in vowels:
      count_vowels=count_vowels+1

if count_vowels == 0:
      print("No vowels found")
else:
      print("The statement has ",count_vowels, "vowels")
