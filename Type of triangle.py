i1=int(input("Enter the first side of triangle"))
i2=int(input("Enter the first side of triangle"))
i3=int(input("Enter the first side of triangle"))

if(i1==i2 and i2==i3):
    print("Its a equilateral triangle")
elif(i1!=i2 and i2==i3):
    print("Its a Isoceles triangle")
elif(i1!=i3 and i1==i2):
    print("Its a Isoceles triangle")
else:
    print("Its a scalar triangle")