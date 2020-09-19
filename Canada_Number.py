n=int(input("Enter a number : "))
def num(n):
	s=0
	while(n>0):
		r=n%10
		s=s+r**2
		n=n//10
	return (s)
def Canada(n):
	s1=0
	for i in range(1,n+1):
		if n%i==0:
			s1+=i
	if (s1-1-n)==num(n):
		return True
	else:
		return False
print(Canada(n)) 
