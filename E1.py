i1=int(input("Enter the Number one for swapping"))
i2=int(input("Enter the Number two for swapping"))

i3=i1
i1=i2
i2=i3

print("Swapping of i1 is" +str(i1))
print("Swapping of i2 is" +str(i2))

# without the third value
i1=i1+i2
i2=i1-i2
i1=i1-i2
print("Swapping of i1 is" +str(i1))
print("Swapping of i2 is" +str(i2))