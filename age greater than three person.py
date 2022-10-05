x=int(input("Enter first age :"))
y=int(input("Enter second age :"))
z=int(input("Enter third age :"))

if x>=y and x>=z:
  print("Oldest is",x)
elif y>=x and y>=z:
  print("Oldest is",y)
elif z>=x and z>=y:
  print("Oldest is",z)
else:
  print("All are equal")	
