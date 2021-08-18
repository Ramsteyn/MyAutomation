# We need to use both try and except both in the Statement
try:
    a=int(input("Enter the value 1"))
    b=int(input("Enter the value 2"))
    c=a+b
    print(c)
except:
    print("Entered a invalid number")
# Finally is not mandattory to use in the code
finally:
    print("This is other part of the Second code code")