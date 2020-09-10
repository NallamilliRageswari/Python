#prime number in between range.
import math
a=int(input("Enter starting  number : "))
b=int(input("Enter ending number :"))
for n in range(a,b+1):
    for i in range(2,abs(int(math.sqrt(n)))+1):
        if n%i==0:
            break
    else:
        print(n,end=" ")

		

