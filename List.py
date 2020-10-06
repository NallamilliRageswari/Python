#all zeros in entered list are add at last of the  list. 
#list=[2,0,4,0,4,5]
#[2,4,4,5,0,0]
a=list(map(int,input("Enter numbers into list: ").split()))
for i in range(0,len(a)):
	if a[i]==0:
		x=a.pop(i)
		a.append(x)
print("New list after add zeros at last:"+str(a))
