# Return a new list that is a shallow copy of the original. This is crucial when you
# want to modify a list without affecting its source.


original_list = [10,20,30]
new_list = original_list.copy()

print("Original list :",original_list)

new_list.append(40) #Modified new list 
new_list.append(70)

print("\nNew List :",new_list)
