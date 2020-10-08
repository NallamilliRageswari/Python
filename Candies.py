#Candies problem:
def Candy(candies,extraCandies)->bool:
    maxCandies = max(candies) - extraCandies
    for i in candies:
        if i >= maxCandies:
            yield True
        else:
            yield False
candies = list(map(int,input("Enter candy in to list:").split()))
extraCandies = int(input("Enter Extra Candies:"))
g_pairs = list(Candy(candies,extraCandies))
print(g_pairs)
