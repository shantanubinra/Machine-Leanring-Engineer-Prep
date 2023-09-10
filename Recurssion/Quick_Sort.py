def pivot_element_sequence(low,high,array):
    """
    Return the Pivot index
    
    """
    pivot_element= array[low]
    i=low
    j=high
    while i<j:
        while (array[i]<pivot_element)&(i<=high):
            i+=1
        while(array[j]>pivot_element)&(j>=low):
            j-=1
        
        array[i],array[j]=array[j],array[i]

        if j<i:
            array[j],array[0]=array[0],array[j]
        
    return j,array

def Quick_sort(low,high,array):
    """
    
    
    """
    if low<high:
        pivot_index,array = pivot_element_sequence(low,high,array)
        Quick_sort(low,pivot_index,array)
        Quick_sort(pivot_index,high,array)
    return array

def main():
    array =[18,2,9,6,1,3,4]

    print(Quick_sort(0,len(array)-1,array))
    
    
if __name__=="__main__":
    main()  #/mnt/d/programming/CODE/Subsequences.py

    