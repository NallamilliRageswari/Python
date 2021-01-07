#Generate Primes using seive function
n=1000001
def seive_gen():
    seive=[1 for i in range(n)]
    i=2
    while(i*i <= n+1):
        if seive[i]==1:
            for j in range(i*i,n,i):
                seive[j]=0
        i+=1
    seive[0]=0
    seive[1]=0
    return seive
seive=seive_gen()
c=int(input())
for _ in range(c):
    d=int(input())
    for i in range(d+1):
        if seive[i]==1:
            print(i,end=" ")
    print()
    


    
       
