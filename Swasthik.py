n=int(input("enter odd number"))
for i in range(n):
	for j in range(n):
		if(j==n//2 or i==n//2 or i<=n//2 and j==0 or i==0 and j>=n//2 or i==n-1 and j<=n//2 or i>n//2 and j==n-1):
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()
