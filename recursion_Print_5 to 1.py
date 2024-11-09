# Print Number from 5 to 1 using Recursion

def printNum(num):
    if(num == 0):
        return
    
    print(num)
    printNum(num -1)

printNum(5)