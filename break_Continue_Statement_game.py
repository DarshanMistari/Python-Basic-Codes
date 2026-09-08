""" 
Take Numbers as input from the user one by one .
Skip negative Numbers, and keep adding the positive ones.
Stop when the user enter 0 and print the total.
(use both break and continue)
"""

total = 0

while True:
    num = int(input("Enter the Number :"))
    if num == 0:
        break   
    if num < 0:
        continue
    total += num  # add only positive Number
print("Total :",total) 