def check_if_sorted(arr,n):

    if (n==0 )|(n==1):
        return True
    elif arr[1]<arr[0]:
        return False
    return check_if_sorted(arr[1:],n-1)

def sum_of_array(arr,n):
    # if n<0:
    #     return summation
    # summation+=arr[0]
    # return sum_of_array(arr[1:],n-1,summation)
    if n==0:
        return 0
    elif n==1:
        return arr[0]
    summation = arr[0]+sum_of_array(arr[1:],n-1)
    return summation


if __name__=='__main__':
    arr =[8,3,4,5,6]
    n=len(arr)-1
    print(check_if_sorted(arr,n))
    print(sum_of_array(arr,n+1))



    
    