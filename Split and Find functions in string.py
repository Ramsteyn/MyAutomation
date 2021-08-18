i="Ramadhas Manimaran is Device associate in amazon is"
print(i.find("ma"))
j=0

for m in i:
    if m=="ma":
        j+=1
print(j)

l=i.split(" ")
for k in l:
    if (k=="is"):
        j+=1
print(j)