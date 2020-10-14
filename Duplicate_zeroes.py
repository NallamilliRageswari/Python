#Duplicate zeroes
a=list(map(int,input("Enter a numbers into list: ").split()))
s=[]
for i in range(len(a)):
    if a[i]!=0:
        s.append(a[i])
    else:
        s.extend([a[i],0])
print(s[:len(a)])
