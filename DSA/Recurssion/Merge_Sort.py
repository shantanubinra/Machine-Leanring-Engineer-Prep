# def Merge_array(array);



def Merge_array(left,right,mid,array):
    """
    Return the Sorted Merged array

    Points to be Noted: Please check on the values for right, for loop it will be(right+1)
    Check for the  while condition line 16
    """
    # print(left,right,mid,array,array[left],array[right],array[mid],array[mid+1],mid+1)
    temp_array=[]
    low=left
    high = mid+1
    while (low<=mid)&(high<=right):
        print(low,high,"low-high")
        if array[low]<=array[high]:
            temp_array.append(array[low])
            low+=1
        else:
            temp_array.append(array[high])
            high+=1
    # print(temp_array,"temp_array")
    

    while low<=mid:
        temp_array.append(array[low])
        low+=1
    while high<=right:
        temp_array.append(array[high])
        high+=1
    for i in range(left,(right+1)):
        array[i]=temp_array[i-left]  

    # array[left:right] = temp_array[left:(right+1)]
    # print(temp_array,"temp_array2")
    # print(array,"array")
    return array


def Divide_array(left,right,array):
    """
    Returns the Smallest eleemnt of the array
    [1,5,6,1,2,3,0,4]
    
    """
    if left==right:
        return 
    mid=(left+right)//2
    Divide_array(left,mid,array)
    Divide_array(mid+1,right,array)
    array = Merge_array(left,right,mid,array)

    return array

def main():
    array =[1,5,6,1,2,3,0,4]

    print("The sorted array is",Divide_array(0,len(array)-1,array))
    
    
if __name__=="__main__":
    main()  #/mnt/d/programming/CODE/Subsequences.py

    