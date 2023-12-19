#interest rate calculate in days
from datetime import date
s=date(2019,1,1)
e=date(2020,1,1)
d=e-s
y=print(d.days)
n=float(input("Enter The Interest Amount:"))
r=float(input("Rate Of Interest:"))
t=float(input("Enter The No.of days:"))
#t=None,(print(d.days))
T=float(n*r*((t*12)/365))/100
S=float(T+n)
print("Total Interest Rate Of Money is:",T)
print("Total Interest Amount is:",S)

# Updated the code Auto assign the time 



from datetime import date
s=date(2022,10,20)
e=date(2023,10,20)
d=(e-s).days
print(d)
n=float(input("Enter The Interest Amount:"))
r=float(input("Rate Of Interest:"))
#t=float(input("Enter The No.of days:"))
#t=None,(print(d.days))
p=((d*12)/365)
# Calculate interest for the given number of days
T= float(n * r * p) / ( 100)   # This  one is modified
#T=float(n*r*((t*12)/365))/100 this is my original formula
S=float(T+n)
print("Total Interest Rate Of Money is:",T)
print("Total Interest Amount is:",S)


