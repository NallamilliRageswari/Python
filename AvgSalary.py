""" Take maximum salary and minimum salary from the given list and,
then return that average of salary."""

arr=list(map(int,input().split()))
Avgsal=sum(arr[1:-1])/(len(arr)-2)
print(Avgsal)
