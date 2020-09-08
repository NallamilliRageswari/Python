a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
i=1
gcd=1
while(i<=min(a,b)):
    if a%i==0 and b%i==0 :
        gcd=i
    i+=1
print("GCD = ",gcd)
