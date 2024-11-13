#String Slicing Accessing Part String
Name = "Hello EveryOne My Name is Darshan"

N1 = slice(0,5)
print(Name[N1])

N2 = slice(17,len(Name))
print(Name[N2])

N3 = slice(10)
print(Name[N3])

#Negative Slicing
N4 = slice(-10)
print(Name[N4])

N5 = slice(-15,-1)
print(Name[N5])
