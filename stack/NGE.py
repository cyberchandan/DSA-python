# next greatest element


def NextGreatestElement(arr):
    stack=[]
    result=[-1]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        if(len(stack)==0):
            result[i]=-1
            stack.append(arr[i])
        elif(stack[-1]>arr[i]):
            result[i]=stack[-1]
            stack.append(arr[i])
        else :
            while(len(stack)>0 and stack[-1]<=arr[i]):
                stack.pop()
            if(len(stack)!=0):
                result[i]=stack[-1]
                stack.append(arr[i])
            else:
                result[i]=-1
                stack.append(arr[i])
    return result

arr=[3,4,5,8,4,3,9,5]
print(NextGreatestElement(arr))
