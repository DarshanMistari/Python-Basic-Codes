# Ask a number from the user. and print all the factors.

num = int(input("Enter the Number :"))
i=1

while i <=num:
    if num % i == 0:
        print(i, end=" ")
    i += 1