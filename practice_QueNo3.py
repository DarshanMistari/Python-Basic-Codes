# Take the user's age as input. Check and print whether they eligible to vote
# (age >= 18) and whether they are senior citizen (age >= 60) print both Resut.

age = int(input("Please Enter your Age :"))

can_vote = age >= 18
senior_citizen = age >= 60

print(f"User can vote :{can_vote}")
print(f"User is senior Citizen :{senior_citizen}")
