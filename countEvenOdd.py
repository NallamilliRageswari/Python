#To check count of even and odd in given number.
def countEvenOdd(n):
    even_count,odd_count=0,0
    while(n):
        r=n%10
        n=n//10
        if(r%2==0):
            even_count+=1
        else:
            odd_count+=1
    print("odd count--",odd_count, "and", "even count--",even_count)
            
n=int(input("Enter a number--"))
countEvenOdd(n)
