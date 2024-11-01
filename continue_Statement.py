# Print the Odd Numbers

num  = int(input("Enter the Number :"))
i = 1
while i <= num:
    if(i % 2 == 0):
        i +=1 
        continue
    print(i)
    i += 1