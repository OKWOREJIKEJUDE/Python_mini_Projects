

#A python program that converts binary(101) to decimal(5)
def binary_to_decimal(binary_number):
    decimal_number = 0
    binary_number = str(binary_number)[::-1]  # Reversing the binary number
    for i in range(len(binary_number)):
        if binary_number[i] == '1':
            decimal_number += 2 ** i
    return decimal_number

# Take binary input from the user
binary_input = input("Enter a binary number: ")

# Check if the input is a valid binary number
if set(binary_input) <= {'0', '1'}:
    decimal_output = binary_to_decimal(binary_input)
    print(f"The decimal equivalent of {binary_input} is {decimal_output}")
else:
    print("Invalid binary number entered.")
