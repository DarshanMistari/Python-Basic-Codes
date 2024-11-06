# Write a Function to find Factorial Number


def calc_fact(num):
    fact =1
    for i in range(1 , num+1):
        fact *= i
    print("Factorial Number:",fact) 
    return fact

calc_fact(5)