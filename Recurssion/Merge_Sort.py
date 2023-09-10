def Merge_array(left,right,mid,array):
    """
    Return the Sorted Merged array
    """
    print(left,right,mid,array,array[left],array[right],array[mid],array[mid+1],mid+1)
    temp_array=[]
    low=left
    high = mid+1
    while (low<=mid)&(high<=right):
        print(low,high)
        if array[low]<array[high]:
            temp_array.append(array[low])
            low+=1
        else:
            temp_array.append(array[high])
            high+=1
    if low==mid:
        temp_array.extend(array[high:(right+1)])
    elif high==right:
        temp_array.extend(array[low:(mid+1)])    

    array[left:right] = temp_array[left:(right+1)]
    return array


def Divide_array(left,right,array):
    """
    Returns the Smallest eleemnt of the array
    [1,5,6,1,2,3,0,4]
    
    """
    if left==right:
        return 
    mid=(left+right)//2
    # print(mid)
    Divide_array(left,mid,array)
    Divide_array(mid+1,right,array)
    array = Merge_array(left,right,mid,array)

    return array

def main():
    array =[18,2,9,6,1,3,4]

    print(Divide_array(0,len(array)-1,array))
    
    
if __name__=="__main__":
    main()  #/mnt/d/programming/CODE/Subsequences.py

    