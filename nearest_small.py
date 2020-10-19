#nearest smallest from right
arr=[8,4,6,2,3]
stack=[]
vec=[]
top=-1
for i in range(len(arr)-1,-1,-1):
    if(top==-1):
        vec.append(arr[i])
    elif(arr[i]>stack[top]):
        vec.append(arr[i]-stack[top])
    elif(arr[i]<=stack[top]):
        while(arr[i]<=stack[top]):
            stack.pop()
            top-=1
            if(top==-1):
                break
        if(top==-1):
            vec.append(arr[i])
        else:
            vec.append(arr[i]-stack[top])
    stack.append(arr[i])
    top+=1
print(vec[::-1])
