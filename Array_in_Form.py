"""given the array nums consisting of 2n elements in the form
[x1,x2,..,xn,y1,y2,..yn].
return the array in the form [x1,y1,x2,y2,...xn,yn].
example-1:
inpt:nums=[2,5,1,3,4,7],n=3
output:[2,3,5,4,1,7]"""
nums=list(map(int,input().split()))
n=int(input())
result = []
for i in range(n):
	result.append(nums[i])
	result.append(nums[i + n])
print(result)
