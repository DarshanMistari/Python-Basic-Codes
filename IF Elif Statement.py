marks = float(input("Enter the Student Marks :"))

if(marks >= 90):
    print("Student is Pass A++ Gread.")

elif(marks >= 80 and marks < 90):
    print("Student is Pass A Gread")
    
elif(marks >= 70 and marks < 80):
    print("Student is Pass B+ Gread")    
    
elif(marks >= 60 and marks < 70):
    print("Student is Pass B Gread.")
    
elif(marks >= 35 and marks < 50):
    print("Student is Pass C Gread.")         

else:
    print("Student is Fail.")