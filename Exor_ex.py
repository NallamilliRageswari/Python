#n=4
#start=3
#output:8
#explaination:array nums is equal to [0,2,4,6,8] where [0^2^4^6^8] exor operation .
n=int(input("Enter a number :"))
start=int(input("Start number:"))
x=0
for i in range(n):
	x^=start+(2*i)
print("after applying exor operation:"+str(x))
