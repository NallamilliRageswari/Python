'''
5. Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:

2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''
a=input()
l=a.split()
l.sort()
b=[]
count1=[]
for i in l:
    if(i not in b):
        b.append(i)
        count1.append(l.count(i))
for i in range(len(b)):
    print(b[i],":",count1[i])
    '''
    f={}
    a=input().split()
    for i in a:
        f[i]=a.count(i)
    res = list(f.keys())
    res.sort()
    for j in res:
        print(j+':',a.count(j))
    '''
