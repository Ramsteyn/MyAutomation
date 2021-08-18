# Creation of object for the file Class
obj = open("C:/Users/ramadhma/Selenium/read.txt" ,'r')
#print(obj.read())

# Reading only Consecutive line of the Text

#print(obj.readline())
#print(obj.readline())
#print(obj.readline())

# Reading only number of characters

#print(obj.read(10))

# "For" loop for reading file
#for i in  obj.read():
        #print(i, end="")

# Reading file line by line in while loop

s=obj.readline()
while(s):
   print(s)
   s=obj.readline()

