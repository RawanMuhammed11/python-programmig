def reverse_string(input_string):

    reversed_string = ''

    reversed_string = char + reversed_string
    return reversed_string

def main():

    user_input = input("Enter your string: ")


    reversed_result = reverse_string(user_input)


    print(f"The reversed string without reversing spaces is: '{reversed_result}'")

if __name__ == "__main__":
    main()