# print start to end, Number is divisible by 3 and 4

start = int(input("Enter Start Number :"))
end = int(input("Enter End Number :"))
i = start
while i <= end :
    if i % 3 == 0 and i % 4 == 0:
        print(i ,end=" ")
    i +=1
