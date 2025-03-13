def Binary_search_floor(arr,target):

    left=0
    right = len(arr)-1
    ans=-1

    while(left<=right):
        mid =(left+right)//2
        print(left,right,mid,arr[mid])
        if arr[mid]<=target:
            ans=mid
            left = mid+1
        else:
            right = mid-1
    return ans




def Binary_search_ceil(arr,target):

    left=0
    right = len(arr)-1
    ans=-1

    while(left<=right):
        mid =(left+right)//2
        print(left,right,mid,arr[mid])
        if arr[mid]<=target:
            # ans=mid
            left = mid+1
        else:
            ans=mid
            right = mid-1
    return ans

def Binary_floor_ceil(arr,target):
    left=0
    right = len(arr)-1
    ans_floor=-1
    ans_ceil =-1
    while(left<=right):
        mid =(left+right)//2

        if arr[mid]<=target:
            ans_floor=mid
            left=mid+1
        else:
            ans_ceil=mid
            right=mid-1
    return ans_ceil,ans_floor




arr=[1,3,5,6]#[1 ,2 ,8 ,10, 10, 12, 19]
print("-----",Binary_search_floor(arr, 2))
print("-----",Binary_search_ceil(arr, 2))
print("-----",Binary_floor_ceil([1,3,5,6], 2))