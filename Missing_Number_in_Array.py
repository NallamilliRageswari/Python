'''Missing Number in Array:
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

Example 1:

Input:
N = 5
A[] = {1,2,3,5}
Output: 4
Example 2:

Input:
N = 10
A[] = {1,2,3,4,5,6,7,8,10}
Output: 9
'''

def missing(array,n):
    s1,s2=0,0
    for i in range(1,n+1):
        s1+=i
    for j in array:
        s2+=j
    return(s1-s2)

n=int(input())
array=list(map(int,input().split()))
c=missing(array,n)
print(c)
