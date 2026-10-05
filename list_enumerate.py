"""enumerate : when you need to acces the index and the value of items 
while through a list. python built in enumrate() function"""


nums = [10,20,30,40,45,53,56,78,98,67,23,67,78,34,9,45]

for index , value in enumerate(nums):
    print(f"Index :{index}  and Value :{value}")
