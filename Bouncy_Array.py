l=list(map(int,input().split()))
j=True
for i in range(len(l)-1):
    if l[i]<l[i+1] and i%2==0:
        continue
    elif l[i]>l[i+1] and i%2!=0:
        continue
    else:
        j=False
        break
print(j)
