# Take a year as input. Check if it is a leap year. 
# A year is a leap year it is divisible by 4,but not by 100, 
# unless it is also divisible by 400.

year = int(input("Please Enter Year :"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It is Leap Year.")
else:
    print("It is Not a Leap Year.")