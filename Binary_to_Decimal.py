# Convertion from  binary number  to decimal number
n=int(input("Enter a Binary number : "))
d=0
b=1
while n:
	r=n%10
	n=n//10
	d+=r*b
	b*=2
print("Decimal number is : ",d)
