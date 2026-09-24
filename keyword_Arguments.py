"""
Keyword arguments let you pass value to a function by explicitly naming 
the parameter. This means you can pass the in any order you are no longer 
dependent on position
"""

def caculate_marks(maths,eng,computer=0,java=0,python=0): 
    print(f"maths = {maths}")
    print(f"eng = {eng}")
    print(f"computer = {computer}")
    print(f"java = {java}")
    print(f"python = {python}")
    total = maths + eng + computer + java + python
    print(f"Total Marks :{total}")

    
caculate_marks(maths=56,computer=45,python=43,eng=56,java=56)
