# Dictionary Method in Python
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
#Return all Keys in Dictonary
print("All Key in Dictionarys :",Student.keys())

#Get Key in Dictionary
print("Get Key in Dictionary :",Student.get("Name"))

#Return  All Values in Dictionarys
print("All Value in Dictionary :",Student.values())

#Return key and Value
print("Return Key and Vlaues :",Student.items())

#Update the Dictionary
new_stud={
    "Email-id" : "darshan@gmail.com"
}
print("Update the Dictionary :",Student.update(new_stud))