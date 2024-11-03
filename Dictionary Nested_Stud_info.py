#Nested Dictionary in Python Store the Student Information
# This Syntax in Nested Dictionary
Student = {
    "Name" : "Darshan Mistari",
    "id" : "3774986",
    "Mobile-No" : "7666xxxx51",
    
    "Marks" : {
        "Java" : 92,
        "Asp.Net" :94,
        "D-S" : "80",
        "CPP" : 95
    }
}

print("Display Nested Dictionary :",Student)

print("Lenght of Dictionary :",len(Student))

#Access All Subject Marks
print("All Subject Marks :",Student["Marks"])

#Access the Java Mark in Nested Dictionary
print("Access Java Marks :",Student["Marks"]["Java"])

