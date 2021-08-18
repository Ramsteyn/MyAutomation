i=int(input("Enter the table number"))

for j in range(1,11):
    if (i*j%3==0 or i*j%5==0 or i*j%7==0):
        continue
    else:
        print(i*j)