
#write a python program that calculates and prints the area of a pentagon give its apothem and side lengths

# Function to calculate area of a regular pentagon
def pentagon_area(apothem, side_length):
    # Calculate perimeter
    perimeter = 5 * side_length
    # Calculate area using the formula: 1/2 * Perimeter * Apothem
    area = 0.5 * perimeter * apothem
    return area

# Input: apothem length and side length
apothem = float(input("Enter the apothem length: "))
side_length = float(input("Enter the side length: "))

# Calculate and print the area of the pentagon
area = pentagon_area(apothem, side_length)
print("The area of the pentagon is: {:.2f}".format(area))
