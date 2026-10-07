""" list method we built in fuction that operate directly on a list.
Allowing you to modify it in place. Unlike built in fuction like sorted which 
return new list,method change the original list."""

# Adding Element: append() : Add sungle Elements to the end of the list.
print("****** List Method in Python ******")
print("\nAdding Element 'append()' Method :")
fruit = ["apple","mango"]
print(f"Original List :{fruit}\n")
fruit.append("grapes")
print(fruit)
fruit.append("orange")
print(fruit)

# Remove Element : remove() : Remove the first ocurance of a specific value of list
# if the item is not found it remains a valuesError
print("\nRemoving Element 'remove()' Method :")
fruits = ["apple","mango","grape","orange","mango"]
print(f"Original List :{fruits}\n")
fruits.remove("mango")
print(fruits)
fruits.remove("orange")
print(fruits)

# Insert Element: insert() : insert an element at a specific index. 
# the first argument is the index, the second is the value.
print("\nInserting Element 'insert()' Method :")
fruits1 = ["apple","mango","grape","orange","mango"]
print(f"Original List :{fruits1}\n")
fruits1.insert(3,"Banana")
print(fruits1)
fruits1.insert(5,"stoberi")
print(fruits1)

# Remove Elements By index : pop() :Remove and return the element at a 
# given index.if no indexid specified.it removes and return the last element.\

print("\nRemoving Element By Index'pop()' Method :")
fruits2 = ["apple","mango","grape","orange","mango"]
print(f"Original List :{fruits2}\n")
pop_last = fruits2.pop()
print(f"Last Elements Remove :{fruits2}")
pop_first = fruits2.pop(0)
print(f"First Elements Remove :{fruits2}")