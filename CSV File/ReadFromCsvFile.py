import csv

f = open("C:/Users/ramadhma/Selenium/Ram.csv")
csv_data= csv.reader(f)
list1=list(csv_data)
print(list1)
print(len(list1))

for row in list1:
   l=len(row)
#   print(l)
   for j in range (0,l):
       if j>=(l-1):
           print(row[j] + " ", end="\n")
       else:
           print(row[j] + " ", end=" ")


#l=len(list1)

#for i in range (0,l):
   # print(list1[i][0]+" ",end="")
   # print(list1[i][1]+" ",end="")
    # print(list1[i][2]+" ",end="\n")