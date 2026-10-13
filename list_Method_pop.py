# Remove Elements By index : pop() :Remove and return the element at a 
# given index.if no indexid specified.it removes and return the last element.\

print("\nRemoving Element By Index'pop()' Method :")
fruits2 = ["apple","mango","grape","orange","mango"]
print(f"Original List :{fruits2}\n")
pop_last = fruits2.pop()
print(f"Last Elements Remove :{fruits2}")
pop_first = fruits2.pop(0)
print(f"First Elements Remove :{fruits2}")