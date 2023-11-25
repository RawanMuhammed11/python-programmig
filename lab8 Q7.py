def reversefun(originalString):
    reverseString=''
    for char in originalString:
            reverseString=char+reverseString
    return reverseString

def main():
    originalString=input("enter the original string :")
    result=reversefun(originalString)
    print(f"the reversed string is :{result}")

if __name__=="__main__":
    main()
