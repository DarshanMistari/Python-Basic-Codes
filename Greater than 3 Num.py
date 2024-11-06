Num1 = int(input("Enter the First Number :"))
Num2 = int(input("Enter the Second Number :"))
Num3 = int(input("Enter the Third Number :"))

if(Num1 >= Num2 and Num1 >= Num3):
    print("First Number is Largest :",Num1)

elif(Num2 >= Num3):
    print("Second Number is Largest :",Num2)
    
else:
    print("Third Number is Largest :",Num3)    