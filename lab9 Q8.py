# first,function to check errors
def error_check():
    length=0
    while length<=0:  # looping  when user enter negative numbers until user enter positive number or when enter any character until enter numeric value
        valid_input=input('please enter length in feet :')
        #to make sure that the user enters a numeric(positive onlyyyy )values
        if valid_input.isdigit():
            length=int(valid_input)
        else:
            print("invalid input ,enter numeric values")

    return length

#second,function to convert feet to meters and print only not return anyvalue

def conversion(length):
    print('feet \t\t meter')
    for feet in range(1,length+1):
        meters = feet * 0.3048
        print(f"{feet}\t\t{meters:.4f}")

def main():
    length=error_check()
    conversion(length)

if __name__ == "__main__":
    main()
