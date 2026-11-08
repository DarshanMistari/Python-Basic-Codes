# A student scored marks in 3 subject. take all there as input,
# calculate the total and average, and print both usinf an f_string.

sub1 = int(input("Enter marks in subect 1 :"))
sub2 = int(input("Enter marks in subect 2 :"))
sub3 = int(input("Enter marks in subect 3 :"))

total = sub1 + sub2 + sub3
avg = total / 3

print(f"Total Scored : {total}  \nAverage is {avg:.2f}")
