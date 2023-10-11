
#todo Implement a program that converts a given decimal number to binary, octal, and hexadecimal.

# Get decimal input from the user
decimal_number = int(input("Enter a decimal number: "))

# Convert to binary, octal, and hexadecimal
binary_number = bin(decimal_number)
octal_number = oct(decimal_number)
hexadecimal_number = hex(decimal_number)

# Display the results
print(f"Binary representation: {binary_number}")
print(f"Octal representation: {octal_number}")
print(f"Hexadecimal representation: {hexadecimal_number}")
