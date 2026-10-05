# Print Only Even Numbers in list 

nums = [10,20,30,40,45,53,56,78,98,67,23,67,78,34,9,45]

n = len(nums)
i=0
print("Evens Numbers in List : ")

while i <= n-1:
    if  nums[i] % 2==0:
        print(nums[i],end=" ")
    i +=1
 