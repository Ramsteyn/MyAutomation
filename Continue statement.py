i=int(input("Enter the number"))
for e in range(1,11):
    if(e*i%6==0):
        continue
    print(e*i)