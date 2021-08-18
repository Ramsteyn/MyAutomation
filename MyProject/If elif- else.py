num=input("enter the number: ")
num=int(num)

if(num<0):
    print("Number is lesser than Zero")
elif(num==0):
    print("Number is Zero")
elif(num%2==0):
    print("Number is even")
elif(num%2==1):
    print("Number is odd")