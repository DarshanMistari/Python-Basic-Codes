# Take as user input start to end
# print the Even Number using while loop

start = int(input("Enter Start Number :"))
end = int(input("Enter End Number :"))
i = start
while i <= end :
    if i % 2 == 0:
        print(i ,end=" ")
    i +=1
