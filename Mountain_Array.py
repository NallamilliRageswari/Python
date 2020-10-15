l=list(map(int,input().split()))
if l.index(max(l))==len(l)-1:
    print("False")
else:
    for i in range(0,l.index(max(l))-1):
        if not l[i]<l[i+1]:
            print("False")
            break
    else:
        for i in range(l.index(max(l)),len(l)-1):
            if not l[i]>l[i+1]:
                print("False")
                break
        else:
             print("True")
