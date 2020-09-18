import math 
def BeattySequence(n): 
    for i in range(1, n + 1): 
        ans = math.floor(i * math.sqrt(2)) 
        print(ans, end = ' ') 
n = int(input("Enter number : "))
BeattySequence(n) 
