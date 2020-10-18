"""To print according to the length of the given number."""
""" Method 1 """
def len(n):
    count=0
    while n>0:
        count+=1
        n=n//10
    return count
def armstrong(n):
    arm=0
    n1=n
    l=len(n)
    print(l)
    while n>0:
        rem=n%10
        arm+=rem**l
        n//=10
    if n1==arm:
        return('armstrong')
    else:
        return('not a armstrong')
n=int(input('enter a number: '))
print(armstrong(n))

""" Method 2 """
def armstrong(n):
    x=1
    while n % 10**1 != n:
        x +=1
    res=0
    temp=n
    while n>0:
        res += (n%10)**x
        n//=10
    return res == temp
print(armstrong(int(input("enter a number"))))
