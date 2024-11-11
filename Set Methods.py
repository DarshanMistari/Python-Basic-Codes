#Set Method in Python

Marks = {"D-S",80,"Java",89,"Asp.net",94,96,"Java",98,89}

Marks2 = {89,69,69,79,90,78,"Java",94,98}

Marks.add("CPP")
print("Add Element in Set :",Marks)

Marks.add("Python")
print("Add Elements in Set :",Marks)

Marks2.remove(78)
print("Remove Element in Set :",Marks2)

Marks.pop()
print("POP Elememt in Set :",Marks)

print("Union in Set :",Marks.union(Marks2))

print("Intersection of set :",Marks.intersection(Marks2))