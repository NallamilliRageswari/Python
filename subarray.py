# This code is  to print subarrays in the list.
n=int(input("Enter number: "))
arr=list(map(int,input().split()))
for i in range(0,n):
    for j in range(i,n):
        for k in range(i,j+1):
            print(arr[k],end=" ")
        print()

'''
For Example:
n=5
arr=[1,2,3,4,5]
then output is 

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
2 
2 3 
2 3 4 
2 3 4 5 
3 
3 4 
3 4 5 
4 
4 5 
5 
'''
   
