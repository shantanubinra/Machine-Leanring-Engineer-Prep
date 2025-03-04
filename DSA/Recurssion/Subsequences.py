def sub_sequence(current_index,empty_array,array):
    """
    Time complexity: 2^n
    Space complexity: n
    """
    # print("sub sequence")
    if current_index>len(array)-1:
        print(empty_array)
        return empty_array
    
    empty_array.append(array[current_index])
    # print(current_index,"current_index")
    sub_sequence(current_index+1,empty_array,array)
    
    empty_array.remove(array[current_index])
    sub_sequence(current_index+1,empty_array,array)

def sub_sequence_possible(current_index,empty_array,array):
    if current_index>len(array)-1:
        print(empty_array)
        return 1
    
    
    empty_array.append(array[current_index])
    # print(current_index,"current_index")
    left = sub_sequence_possible(current_index+1,empty_array,array)
      
    
    empty_array.remove(array[current_index])
    right = sub_sequence_possible(current_index+1,empty_array,array)
    return left+right


def sub_sequence_sum(current_index,empty_array,array,key_sum,summation_new_array):
    """
    Time complexity: 2^n
    Space complexity: n
    """
    if current_index>len(array)-1:
        if summation_new_array==key_sum:
            print(empty_array,"for sub sequence")
        return 
    
    empty_array.append(array[current_index])
    summation_new_array+=array[current_index]
    sub_sequence_sum(current_index+1,empty_array,array,key_sum,summation_new_array)
    
    empty_array.remove(array[current_index])
    summation_new_array-=array[current_index]
    sub_sequence_sum(current_index+1,empty_array,array,key_sum,summation_new_array)


def only_one_sub_sequence_sum(current_index,empty_array,array,key_sum,summation_new_array):
    """
    Time complexity: 2^n
    Space complexity: n
    """
    if current_index>len(array)-1:
        if summation_new_array==key_sum:
            print(empty_array,"for sub sequence")
            return True
        return False
    
    empty_array.append(array[current_index])
    summation_new_array+=array[current_index]
    if only_one_sub_sequence_sum(current_index+1,empty_array,array,key_sum,summation_new_array)==True:
        return True
    
    empty_array.remove(array[current_index])
    summation_new_array-=array[current_index]
    if only_one_sub_sequence_sum(current_index+1,empty_array,array,key_sum,summation_new_array)==True:
        return True
    
    return  False


def give_count_sub_sequence_sum(current_index,empty_array,array,key_sum,summation_new_array):
    """
    Time complexity: 2^n
    Space complexity: n
    """
    if current_index>len(array)-1:
        if summation_new_array==key_sum:
            # print(empty_array,"for sub sequence")
            return 1

        else: return 0
    
    empty_array.append(array[current_index])
    summation_new_array+=array[current_index]
    left=give_count_sub_sequence_sum(current_index+1,empty_array,array,key_sum,summation_new_array)
    
    empty_array.remove(array[current_index])
    summation_new_array-=array[current_index]
    right=give_count_sub_sequence_sum(current_index+1,empty_array,array,key_sum,summation_new_array)

    return left+right

def sub_sequence_09_12_23(array,current_index,new_Array,n):
    if current_index>n-1:
        print(new_Array)
        return new_Array
    else:
        new_Array.append(array[current_index])
        sub_sequence_09_12_23(array,current_index+1,new_Array,n)
        new_Array.remove(array[current_index])
        sub_sequence_09_12_23(array,current_index+1,new_Array,n)


def main():
    # sub_sequence_09_12_23([3,2,1],0,[],3)
    # print("The total number of subsequence",sub_sequence_possible(0,[],[3,2,1]))
    sub_sequence(0,[],[3,2,1])
    # sub_sequence_sum(0,[],[1,2,1,1,1,3,4],3,0)
    # print(only_one_sub_sequence_sum(0,[],[1,2,1,1,1,3,4],16,0))
    # print(give_count_sub_sequence_sum(0,[],[1,2,1,1,1,3,4],3,0))
if __name__=="__main__":
    main()  #/mnt/d/programming/CODE/Subsequences.py
