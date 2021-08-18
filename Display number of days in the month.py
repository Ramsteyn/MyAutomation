n=input("Enter the number to display number of days in the month")
n=int(n)

if(n>0 and n<=12):
    if(n==2):
        print("The Number of days is 28")
    elif(n==4 or n==6 or n==9 or n==11):
        print("The number of days is 30")
    else:
        print("The number of days is 31")
else:
    print("The number is invalid")

