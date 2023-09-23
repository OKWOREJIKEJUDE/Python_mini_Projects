

#Create a program that asks the user for their age and prints a message indicating if they are a minor, an adult, or a senior.

age = int(input("Enter your age: "))

if age >= 1 and age <= 15:
    print("You are a minor")
elif age >= 16 and age <= 35:
    print("You are an adult")
elif age >= 36 and age <= 120:
    print("You are a senior")
else:
    print("Please enter a positive number age and within the range of 1-120. Thanks")