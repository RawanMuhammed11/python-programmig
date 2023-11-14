for i in range(5):
    weight = float(input('enter the weight:'))
    if weight <0:
        print('invalid weight')
        continue  #to skip this iterate and start again

    unit = int(input('enter the unit (1 for mg, 2 for kg, 3 for ton):'))
    if unit==1:
        print(weight)
        print("converting mg to gram ")
        converted_weight=1/1000*weight
    elif unit==2:
        print('weight')
        print('convering kg to gram')
        converted_weight=1000*weight
    elif unit==3:
        print('weight')
        print("converting ton to gram")
        converted_weight=1000000*weight
    else:
        print("invalid unit")
        continue  #to skip this iterate and start again

    print(converted_weight)
    choice=input("Do you want to another conversion Yes or No ")
    if choice=='no':
        break