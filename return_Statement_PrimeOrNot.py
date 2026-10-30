# return true if a number is prime number return Flase

def is_Prime(num):
    count = 0
    for i in range(1, num+1):
        if num % i ==0:
            count +=1
    if count == 2:
        return True
    else:
        return False
    
num = int(input("Enter the NUmber :"))
prime = is_Prime(num)
print(f"It is Prime Number :{prime}")
