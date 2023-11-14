soup_lst=['vegetables', 'seafood','mushroom']
meal_lst= ['burger', 'grilled chicken', 'mashed potatoes']
vegetables=['vegetables','mushroom','mashed potatoes']
print(soup_lst)
print(meal_lst)
soup = input("Enter the soup > ")
meal = input("Enter the meal >")
# Check for vegetables in the soup and meal
if soup in vegetables and meal in vegetables:
     print("She loves vegetables")
elif soup in vegetables or meal in vegetables:
     print("She neither hate or love vegetables")
else:
    print('she hates vegetables')
