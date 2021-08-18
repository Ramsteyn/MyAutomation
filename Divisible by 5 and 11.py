n=input("Enter the number")
n=int(n)

if(n%5==0 and n%11==0):
    print("The number is divisible by 5 and 11")
elif(n%5==0):
    print("The number is divisible by 5 only")
elif(n%11==0):
    print("The number is divisible by 11 only")
else:
    print("The number is not divisible by 5 and 11")
