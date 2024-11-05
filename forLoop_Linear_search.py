
num =[1 , 4, 9, 15, 20, 25, 22, 45, 35, 60]

x = int(input("Enter Searching Number :"))

idx = 0
for val in num:

    if( val == x):

        print(val,"Number is Found  index:",idx)
    idx += 1