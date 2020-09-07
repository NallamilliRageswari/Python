m=int(input("Enter first number : "))
n=int(input("Enter second number : "))
greater=max(n,m)
while(True):
    if(greater%m==0 and greater%n==0):
        print("LCM = ",greater)
        break
    greater+=1
