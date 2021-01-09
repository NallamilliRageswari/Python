'''
vowel & Constants Count and both multiplied gives result.
Input:
    2
    abcdefg
    scdegh
Output:
    2 5 10
    1 5 5
'''
n=int(input())
for _ in range(n):
    s=input()
    c=0
    v=0
    for j in s:
        if('a'==j or 'e'==j or 'i'==j or 'o'==j or 'u'==j):
            v+=1
        else:
            c+=1
    print(v,c,v*c)

            

