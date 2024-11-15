# Search the Number in the List using While loop.

num = (23, 34, 24, 43, 78, 89, 23,90, 24,45)

x = 24
i = 0
while i < len(num):
    if(num[i] == x):
        
        print("Element is Found index :",i)
        
    else:
        
        print("Element is Not Found.")
        
    i += 1