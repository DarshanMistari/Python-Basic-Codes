# Global Variable 

# global variable can create the outside the block 
# it can access any where in the program

names = "Darshan"  #Global Variable

def greet():
    name = "Kalpesh"
    print(f"Hey {name }! Good Morning")
    print("\nInside the Block :")
    print(f"Hey {names }! Good Morning\n")
    


greet()
print(f"Outside the Block :")
print(f"Hey {names} ! Good Morning")