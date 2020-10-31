"""Compulsory input taken in assending order ,
Target is assigned to the list and sorted list and 
where the target is placed in list return the index value.if the number is
not exist  in list then it raise an error(Index out of range).
Input:
a=[1,3,5,6]
target=4
output:
2
"""

#model-1

a=list(map(int,input().split()))
target=int(input())
if(target in a):
	print(a.index(target))
else:
	a.append(target)
	a.sort()
	print(a.index(target))
	
#model-2

heap,num,itr=list(map(int,input().split())),int(input()),0
while heap[itr]<num:
    itr +=1
print(itr)
