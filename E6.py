i=int(input("Enter the number to find whether prime or not"))

j=0
for k in range(2,i):
    if(i%k ==0):
        print("This number is not a prime")
        j=1
        break
    k+=1
if(j==0):
   print("The number is prime")
