a=list(map(int,input().split()))
b=[]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            b.append(a[i]-a[j])
            break
        else:
            b.append(a[i])
print(b) 
