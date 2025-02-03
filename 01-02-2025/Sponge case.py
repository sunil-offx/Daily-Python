def is_sponge_case(s):
    for i in range(len(s)):
        if i % 2 == 0 and not s[i].isupper():  
            return False
        if i % 2 != 0 and not s[i].islower():  
            return False
    return True

input_string = input("Enter a string: ")
if is_sponge_case(input_string):
    print("True: The string follows the sponge case pattern.")
else:
    print("False: The string does not follow the sponge case pattern.")
