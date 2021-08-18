i1=int(input("Enter the number to Get Fibonacci series"))

j=0
k=1
print(j)
print(k)
while(j+k <i1):
    k=k+j
    j=k-j
    print(k)