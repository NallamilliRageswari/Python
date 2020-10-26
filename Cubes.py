#Using dictionary concept writing code for cubes of a number in between range.
n=int(input("Enter a number: "))
d={i:i**3 for i in range(1,n+1)}
print(d)
