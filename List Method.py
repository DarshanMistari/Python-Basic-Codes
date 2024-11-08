#List Method

marks =[ 33, 89, 45.3, 33.8,]
print("Orignal List :",marks)

marks.append(45)
print("Add Element in List :",marks)

marks.remove(33)
print("Remove Element in List :" ,marks)

marks.reverse()
print("List Reverse :", marks)

marks.sort()
print("List Sort :",marks)

marks.insert(3,"A")
print("Element insert in index :",marks)

print("List Element Pop :", marks.pop(1))
