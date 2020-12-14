'''
4. Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''
f_a=0
while True:
    a=input()
    if not a:
        break
    b=a.split()
    if b[0]=='D':
        f_a = f_a + int(b[1])
    elif b[0]=='W':
        f_a = f_a - int(b[1])
print(f_a)
