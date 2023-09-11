def pivot_element_sequence(low,high,array):
    """
    Return the Pivot index
    
    """
    pivot_element= array[low]
    i=low
    j=high
    while i<j:
        while (i<=high-1)&(array[i]<=pivot_element):
            # print(array,i,j,low,high,"low")
            i+=1

        while (j>=low+1)&(array[j]>pivot_element):
            j-=1
        if i<j:
            array[i],array[j]=array[j],array[i] #swaping the values

    
    array[j],array[0]=array[0],array[j]
    print(j,array)
    return j,array

def Quick_sort(low,high,array):
    """
    Returns the sorted array
    
    """
    if low<high:
        pivot_index,array = pivot_element_sequence(low,high,array)
        Quick_sort(low,pivot_index,array)
        Quick_sort(pivot_index+1,high,array)
    return array

def main():
    array =[1,5,6,1,2,3,0,4]
    # array = [5,9,1,2]
    print(Quick_sort(0,len(array)-1,array))
    
    
if __name__=="__main__":
    main()  #/mnt/d/programming/CODE/Subsequences.py

    