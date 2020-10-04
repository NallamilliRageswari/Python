import math 
def checkPronic (x) :
    i = 0
    while ( i <= (int)(math.sqrt(x)) ) :
        if ( x == i * (i + 1)) :
            return True
        i = i + 1
    return False 
i = 0
n=int(input("Enter a number: "))
print ("Pronic Numbers in between 0 to "+str(n)+" is :")
while (i <= n ) :
    if checkPronic(i) :
        print(i),
    i = i + 1
  
