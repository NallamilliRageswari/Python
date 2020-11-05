"""given an integer array nums of 2n integers,
group these integers into n pairs(a1,b1),(a2,b2),...(an,bn)
such that sum of min(ai,bi) for all i is maximized.
return the maximized sum.

input 1:
nums=[1,4,3,2]
output: 4

input2:
nums=[6,1,3,2,1,7]
output: 9
"""

nums=list(map(int,input().split()))
nums.sort()
print(sum(nums[::2]))
		
