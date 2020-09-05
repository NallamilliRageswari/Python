n=input("Enter a number : ")
x=0
for i in range(len(n)-1):
    if int(n[i])<=int(n[i+1]) and (x==1 or x==0):
        x=1
    elif int(n[i])>=int(n[i+1]) and (x==2 or x==0):
        x=2
    else:
        print(n+" No Order")
        break
else:
    if x==1:
        print(n+" is in Ascending order.")
    else:
        print(n+" is in Descending order.")
