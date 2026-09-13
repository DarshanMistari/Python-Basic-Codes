# A Default Argument is a value that a parameter take automatically 
# if no arguments is passed for it when calling the function. 
# it make certain parameter optional.

#default marks is 0
def caculate_marks(maths,eng,computer=0,java=0,python=0): 
    print(f"maths = {maths}")
    print(f"eng = {eng}")
    print(f"computer = {computer}")
    print(f"java = {java}")
    print(f"python = {python}")
    total = maths + eng + computer + java + python
    print(f"Total Marks :{total}")

caculate_marks(45,23,56,23)