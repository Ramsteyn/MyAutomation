i="Madam"
j="madam"

if(i.lower()==j.lower()):
    print("Value is compared and equal")
else:
    print("Value is not equal")

b=""
l=len(i)
for j in range(l-1,-1,-1):
    b=b+i[j]

print(b.lower())
if b.lower()==i.lower():
    print("Its a palendrome sequence")
else:
    print("Its not a Palendrome sequence")