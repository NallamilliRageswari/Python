def cyclic_permutation(num):
    temp=num
    res=[int(x) for x in str(num)]
    c=len(res)-1
    while(1):
        print(temp)
        r=temp%10
        d=temp//10
        temp=(10**c)*r+d
        if(temp==num):
            break
n=int(input())
cyclic_permutation(n)

