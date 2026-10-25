# True or False Return, If user Can Vote.

def can_Vote(age):
    if age >= 18:
        return True
    else:
        return False
    
age = int(input("Enter Your Age :"))
vote = can_Vote(age)

print(f"User Can Vote :{vote}")