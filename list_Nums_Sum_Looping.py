# Sum of Num in list using for loop

nums = [10,20,30,40,45,53,56,78,98,67,23,67,78,34,9,45]

n= len(nums)
total = 0

for i in range(0,n):
    total = total+ nums[i]

print(f"Sum of List :{total}")