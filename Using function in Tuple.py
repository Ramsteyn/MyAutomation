# Count number of values are same in tuple
t=(34, 34, 'ram', "ram", 54, 45.6 , 'my program')
print(t.count(34))

# find index of any value in tuple
print(t.index('ram'))

# Concation of tuple

t2=(23, 34)
t3=t2+t
print(t3)

# printing values in the tuple using loop
for i in t:
    print(i)

j=len(t)
for j in range(0,j):
    print(t[j])