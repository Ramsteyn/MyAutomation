num=input("Enter the number: ")
num=int(num)

if(num>100 or num<0):
  print("Number is invalid")
elif(num%2==0):
    print("Number is even")
else:
    print("Number is odd")