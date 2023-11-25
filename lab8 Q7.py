def reversefun(originalString):
    reverseString=originalString[::-1]
    return reverseString

def main():
    originalString=input("enter the original string :")
    result=reversefun(originalString)
    print(f"the reversed string is :{result}")

if __name__=="__main__":
    main()
