# Accessing List Elements : Indexing
"""
positive indexing : left to right
Negative indexing : right to left

Update Element in Indexing
"""
name = ["Darshan","Rahul","Dinesh",766,34.45,True,34]

print("Accessing List Elements : Indexing")
print(name)
print("\nFirst Elements :",name[0])

print("\nLast Element :",name[-1])

print("\nThird Element :",name[2])

n = len(name)
print("\nMiddle Element :",name[n//2])

# Update list Element in indexing
name[2] = "Kalpesh"
print("\nUpdated List :",name)