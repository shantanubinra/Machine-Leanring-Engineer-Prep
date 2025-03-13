# from recurssion

def Binary_search_recurssion(arr,left,right,target):
    if left>=right:
        return False
    
    mid=(left+right)//2

    if arr[mid]==target:
        return True
    
    if target>arr[mid]:
        return Binary_search_recurssion(arr,mid+1,right,target)
    if target<arr[mid]:
        return Binary_search_recurssion(arr,left,mid,target)

    
print(Binary_search_recurssion([-1,0,3,5,9,12],0,5,2))

def Binary_search(arr,target):

    left=0
    right = len(arr)-1

    while(left<right):
        print(left,right)
        mid=(left+right)//2
        print(left,right,mid,arr[mid])
        if arr[mid]==target:
            return mid
        elif target>arr[mid]:
            left=mid+1
        elif target<arr[mid]:
            right=mid
    
print(Binary_search([-1,0,3,5,9,12],2))