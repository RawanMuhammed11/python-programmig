friends=input("enter name of friends:").split()
presents=input('enter the name of presents').split()
wanted_present = input("What is in his mind: ")
found=False
for i in range(len(presents)):
    if presents[i]==wanted_present:
      name=friends[i]
      print('oh '+name+' Thank you friend :)')
      found=True
      break
if not found:
  print("Oops, Sorry none.")