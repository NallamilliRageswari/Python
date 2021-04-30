'''
Problem
You are given an array of integers  A, you need to find the maximum sum that can be obtained by picking some non-empty subset of the array. If there are
many such non-empty subsets, choose the one with the maximum number of elements. Print the maximum sum and the number of elements in the chosen
subset.

Input:

The first line contains an integer N, denoting the number of elements of the array. Next line contains  space-separated integers N, denoting the elements of the
array.

Output:

Print 2 space-separated integers, the maximum sum that can be obtained by choosing some subset and the maximum number of elements among all such
subsets which have the same maximum sum.

Constraints:
1<= N <= 10^5
-10^9 <=Ai <=10^9
Sample Input
5
1 2 -4 -2 3
Sample Output
6 3
'''
n = int(input())
arr = list(map(int, input().split()))
sum_arr = count_arr = 0
max_arr = max(arr)
for i in range(n):
    if arr[i] >= 0:
        sum_arr += arr[i]
        count_arr += 1
if(count_arr==0):
    print(max_arr, count_arr+1)
else:
    print(sum_arr, count_arr)
