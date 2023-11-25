def reversefun(originalString):
    reverseString=''
    for char in originalString:
        if char != ' ':   # if user add any spaces in the originalString > skip it and reverse other characters
            reverseString=char+reverseString

    return reverseString

def main():
    originalString=input("enter the original string :")
    result=reversefun(originalString)
    print(f"the reversed string is :{result}")

if __name__=="__main__":
    main()
