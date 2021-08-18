# Specifying index
i=[348, 45.9,"My programe", 489, 'Range']
print(i[2])

# Specifying index range
print(i[2:5])

# Specifying first index only
print(i[1:])

# Specifying last index only
print(i[:5])

# Inserting in the list

i[3]="Number"
i.insert(3,5)
print(i)

# removing values from the list
i.remove("Number")
print(i)

# finding length of the list
j=len(i)
print(j)
i.insert(4,50)
j=len(i)
print(j)

# Concatinate 2 lists
l=[34, 45, 34,'ram']
k=[45, 45.5,"Fuck"]
m=l+k
print(m)
