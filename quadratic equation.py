import cmath
a=int(input("Enter a Number:"))
b=int(input("Enter b Number:"))
c=int(input("Enter c Number:"))
d=(b**2)-(4*a*c)
x1=(-b-cmath.sqrt(d))/(2*a)
x2=(-b+cmath.sqrt(d))/(2*a)
print(x1)
print(x2)

