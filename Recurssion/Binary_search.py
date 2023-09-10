# def _search(arr,n,searching_items):
#     for i in arr:
#         if i==searching_items:
#             return True
#     return False

def binary_search_recurssion(arr,current,low,high,searching_items,n):
    print(low,high)
    if low>high:
        return False
    
    current= (low+high)//2
    if arr[current]==searching_items:
        return True
    if arr[current]>searching_items:
        low = current+1
        return binary_search_recurssion(arr[low:high],current,low,high,searching_items,n)
    if arr[current]<searching_items:
        high = current
        return binary_search_recurssion(arr[low:high],current,low,high,searching_items,n)

    

if __name__=='__main__':
    print(1//2)
    arr =[3,4,5,6,8]
    n=len(arr)
    
    print(binary_search_recurssion(arr,0,0,n,6,n))
    print("Linear search using loop")
    # print(linear_search(arr,n,8))
        