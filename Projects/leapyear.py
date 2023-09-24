

# #Write a Python program that checks if a given year is a leap year or not
# def is_leap_year(year):
#     """
#     Check if a given year is a leap year or not.
    
#     Args:
#         year (int): The year to be checked.
        
#     Returns:
#         bool: True if the year is a leap year, False otherwise.
#     """
#     # A year is a leap year if it is divisible by 4
#     # But if it is also divisible by 100, it should be divisible by 400 to be a leap year
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False

# # Input year from the user
# year = int(input("Enter a year: "))
#  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False

# Check if it's a leap year and display the result
# if year:
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")







# #Write a Python program that checks if a given year is a leap year or not
yearr = int(input("Enter the year:"))
if (yearr % 4 == 0 and yearr % 100 != 0 or yearr % 400 == 0):
    print(f"{yearr} is a leap year")
else:
    print(f"{yearr} is a not leap year")
