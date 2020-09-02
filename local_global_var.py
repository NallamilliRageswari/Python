a=10
print(a,'1')
def ex():
    global i
    i=10
    i+=1
    print(i,'2')
ex()
print(i,'3')
