print("***** Calculator *****")
print("1.Addition \n2.Subtraction \n3.Division \n4.Multiplication \n5.Remainder")

op = int(input("Enter the Operation Digit :"))

Num1 = int(input("Enter the First Number :"))

Num2 = int(input("Enter the Second Number :"))

if(op == 1):
    Sum = Num1 + Num2
    print("Addition :" , Sum)

elif(op == 2):
    Sub = Num1 - Num2
    print("Subtraction :" , Sub)
    
elif(op == 3):
    Div = Num1 / Num2
    print("Division :" , Div)
    
elif(op == 4):
    Mul = Num1 * Num2
    print("Multiplication :" , Mul)  
    
elif(op == 5):
    Rem = Num1 % Num2
    print("Remainder :" , Rem)
    
else:
    print("Invalid OPeraton.")          