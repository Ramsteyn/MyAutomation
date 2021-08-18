tr1="ABCD"
tr2="PQR"
tr3=""
tr4=""
for i in range(4):
    tr3=tr3+tr1[i]
    tr4=tr3+tr2
    tr2=tr2[1:3]
    #print(tr2)
    print(tr4,end="\n")


