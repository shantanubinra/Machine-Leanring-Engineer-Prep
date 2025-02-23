def Selection_sorting(array):
    """
    Time complexity: O(n)*O(n)
    second loops: n*n-1*n-2*n-3...2*1 =n(n+1)/2
    """
    for i in range(len(array)):
        minimum=array[i]
        index_minimum=i
        for j in range(i, len(array)):
            if array[j]<minimum:
                minimum=array[j]
                index_minimum= j
        array[i],array[index_minimum]=array[index_minimum],array[i]
    return array
print("Selection Sorting",Selection_sorting([4,1,5,8,0,3,9,2]))


def Bubble_sorting(array):
    """
    O(n)*O(n)*O(n-1)*O(n-2)....2*1 =O(n^ square)

    # best case --> when the array is already sorted... for that we 
    will put a flag tocheck whether any single time a swap has been happened or not
    """
    for i in range(len(array)):
        did_swap=0
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]= array[j+1],array[j]
                did_swap =1
        
        if !(did_swap):
            break
    return array

print("Bubble Sorting   ",Selection_sorting([4,1,5,8,0,3,9,2]))


def Insertion_Sorting(array):






