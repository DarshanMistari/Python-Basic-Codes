# Print the Even Num in list Using enumerate function

nums = [10,20,30,40,45,53,56,78,98,67,23,67,78,34,9,45]
print("Even NUmbers :")
for index ,value in enumerate(nums):
    if value % 2 == 0:
        print(f"{value}",end=" ")