m=int(input("Enter the Maths mark"))
e=int(input("Enter the English mark"))
p=int(input("Enter the Physiscs mark"))
b=int(input("Enter the Biology mark"))
c=int(input("Enter the Chemistry mark"))

if(m>100 or e>100 or p>100 or b>100 or c>100 or m<0 or e<0 or p<0 or c<0 or b<0):
    print("The entered mark is invalid")
else:
    avg= (m+e+p+b+c)/5
    if(avg>=90):
       print("Your grade is A")
    elif(avg>=80 and avg<90):
       print("Your grade is B")
    elif(avg>=70 and avg<80):
       print("Your grade is C")
    elif(avg>=60 and avg<70):
       print("Your grade is D")
    elif(avg>=50 and avg<60):
       print("Your grade is E")
    elif(avg>=40 and avg<50):
       print("Your grade is F")
