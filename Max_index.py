arr=list(map(int,input().split()))
k=arr.index(max(arr))
c=0
for i in arr[:k]+arr[k+1:]:
    if 2*i<=max(arr):
        c+=1
    else:
        print(-1)
        break
if c==len(arr[:k]+arr[k+1:]):
    print(k)
