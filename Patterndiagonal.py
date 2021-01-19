#Input:5
#Output: x000x
 #       0x0x0
  #      00x00
   #     0x0x0
    #    x000x

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i==j or i+j==(n+1)):
                print('x',end="")
            else:
                print('0',end="")
        print()
    return None
n=int(input())
pattern(n)
