# sort : sorts the elements of the list an asceding order directly. 
# modifying the original list.

# sort() : Original list Modify 
print("sort() : Original list Modify.\n")
nums = [34,23,67,78,45,89,23,78,27,89,67,45,21]
print(f"Original list :{nums}")
nums.sort() # in place sorting
print(f"\nNums Sort list :{nums}")


# sorted() : created new list not original list modify
print("\n\nsorted() : created new list not original list modify.\n")
num1 = [34,67,23,89,56,90,2,20,1,45]
new_list = sorted(num1)

print(f"Original List : {num1} ",id(num1))

print(f"\nNew List : {new_list} ",id(new_list))







