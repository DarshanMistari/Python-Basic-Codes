# 90 above -> A+
# 81 -> 90 -> A
# 71 -> 80 -> B+
# 61 -> 70 -> B
# 35 -> 60 -> C
# 35 -> below -> Fail

marks = int(input("Enter your Marks :"))

if marks >=91 and marks <= 100:
    print("You are Pass, Grade : A+")
elif marks >= 81 and marks <= 90:
    print("You are Pass, Grade : A")
elif marks >=71 and marks <=80:
    print("You are Pass, Grade : B+")
elif marks >=61 and marks <= 70:
    print("You are Pass, Grade : B")
elif marks >= 35 and marks <=60:
    print("You are Pass, Grade : C")
elif marks >= 0 and marks <= 34:
    print("You are Fail")
else:
    print("Invalide Marks Enter,Pleased Try Agains")
