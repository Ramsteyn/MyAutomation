


for i in range(1,6):
    for j in range(1,6):
       if(i==1 or i==5):
         print("*", end="")
       else:
           if (j==1 or j==5):
              print ("*", end="")
           else:
               print(" ", end="")
    print()

for i in range(1, 6):
    for j in range(1, 6):
        if (i==1):
            print("*", end="")
        elif(i==2):
            if ( j <= 4):
                print("*", end="")
            else:
                print(" ", end="")
        elif (i == 3):
            if ( j <= 3):
                print("*", end="")
            else:
                print(" ", end="")
        elif (i == 4):
            if ( j <= 2):
                print("*", end="")
            else:
                print(" ", end="")
        elif (i == 5):
            if ( j <= 1):
                print("*", end="")
            else:
                print(" ", end="")

    print()



for i in range(1, 6):
    for j in range(1, 6):
        if (i==1):
            print("*", end="")
        elif(i==2):
            if ( j>1):
                print("*", end="")
            else:
                print(" ", end="")
        elif (i == 3):
            if ( j>2):
                print("*", end="")
            else:
                print(" ", end="")
        elif (i == 4):
            if ( j>3):
                print("*", end="")
            else:
                print(" ", end="")
        elif (i == 5):
            if ( j>4):
                print("*", end="")
            else:
                print(" ", end="")

    print()