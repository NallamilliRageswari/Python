n=int(input("enter: "))
a=2*n-2
for i in range(n):
	for j in range(0,a):
		print(end=' ')
	a-=1
	for j in range(1,i+1):
		print(j,end='')
	for j in range(0,i+1):
		print(j,end='')
	print()

