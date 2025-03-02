def linear_search(arr,n,searching_items):
    for i in arr:
        if i==searching_items:
            return True
    return False

def linear_search_recurssion(arr,n,searching_items):
    if n==0:
        return False
    
    else:
        if arr[0]==searching_items:
            return True
    return linear_search_recurssion(arr[1:],n-1,searching_items)


if __name__=='__main__':
    arr =[3,4,5,6,8]
    n=len(arr)
    print("Linear search using Recurssion")
    print(linear_search_recurssion(arr,n,8))
    print("Linear search using loop")
    print(linear_search(arr,n,8))
        