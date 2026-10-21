

age = int(input("Please Enter Your Age :"))

has_degree = str(input("Please Enter Your Graduation are Complete, Yes Or No :"))

if age >=18:
    print("Age Requirement Complete")
    if has_degree == "Yes":
        print("You are Eligible for this Job.")
    else:
        print("You are Not Eligible for this Job.")
else:
    print("You are Not Hire,Age is less than 18.")