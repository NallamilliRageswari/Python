#using normal function
def mul(a,b):
    res=0
    while True:
        if(a%2!=0):
            res+=b
        a//=2
        b*=2
        if(a==0):
            break
    return res
a,b=map(int,input().split())
print(mul(a,b))

 
#Using recursion
def mul(a,b):
    if a==0: 
        return 0
    if a%2:
        return b+mul(a//2,b*2)
    else:
        return 0+mul(a//2,b*2)
a,b=map(int,input().split())
print(mul(a,b))

