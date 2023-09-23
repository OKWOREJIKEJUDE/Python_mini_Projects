


#Write a program that checks if a number is even or odd and prints the result.
number = int(input("Enter number:"))

checkings = number % 2
if checkings == 0:
    print(f"The number {number} is an even number")
else:
    print(f"The number {number} is an odd number")