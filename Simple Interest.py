# Calculate the Simple Interest
# p : Principle amount , t : Time of Period , r:Rate of Interest si=Simple Interest

p = float(input("Enter the P Amount :"))
t = float(input("Enter the Time Period :"))
r = float(input("Enter the Rate :"))

si = (p*t*r)/100
print("Interest :",si)