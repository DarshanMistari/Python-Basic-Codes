# Print Number from 1 to 5 using Recursion

def printNum(num):
    if(num == 6):
        return
    print(num)
    printNum(num + 1) 

printNum(1)