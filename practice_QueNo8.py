# Take Two Number as input,Print the Greater of the Two. 
# If they are equal, print "Both are Eqaul".

num1 = int(input("Enter First Number :"))
num2 = int(input("Enter Second Number :"))

if num1 > num2:
    print(f"First Number is Greater than Second Number : {num1}")
elif num2 > num1:
    print(f"Second Number is Greater than First Number : {num2}")
else:
    print("Both are Equal Number")