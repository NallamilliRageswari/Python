#Students stand in line in heightwise and students change place,
#then print the count  of changed places in certain line.
#input:a=[5,1,2,4,3]
#output:4
a=list(map(int,input().split()))
count=0
b=sorted(a)
for i in range(len(a)):
    if b[i]!=a[i]:
        count+=1
print(count)
