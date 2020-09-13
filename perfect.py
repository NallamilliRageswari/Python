#PERFECCT NUMBER
def perfect(n):
    c=0
    for i in range(1,n//2+1):
        if n%i==0:
            c+=i
    if c==n:
        return "True"
    else:
        return "False"
n=int(input("Enter a number"))
print(perfect(n))
