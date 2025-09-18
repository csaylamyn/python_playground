# value = input("enter a value (number or string): ")

# match value:
#     case int():
#         print("you entered an integer: ", int(value))
#     case str():
#         print("you entered string value: ", value)
#     case _:
#         print("invalid data type entered")


value = input("Enter a value (number or string): ")

# First try to interpret it as an integer
try:
    int_value = int(value)
    match int_value:
        case int():
            print("You entered an integer:", int_value)
except ValueError:
    # If not convertible to int, keep it as string
    match value:
        case str():
            print("You entered a string:", value)
        case _:
            print("Invalid data type entered.")



# value = input("Enter a value (number or string): ")

# if value.isdigit():
#     print("You entered an integer:", int(value))
# else:
#     print("You entered a string:", value)
# value = input("Enter a value (number or string): ")

