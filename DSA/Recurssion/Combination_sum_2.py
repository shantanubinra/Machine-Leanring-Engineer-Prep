# https://leetcode.com/problems/combination-sum/

# if index_to_be_picked==len(array)-1:
#     if target==0:
#         print(temp_list)

#     return

# if target<array[index_to_be_picked]:
#     return

# if index_to_be_picked<len(array)-1:
#     target -=array[index_to_be_picked]
#     temp_list.append(array[index_to_be_picked])
#     combination_sum(array,target,index_to_be_picked,final_list,temp_list)
#     temp_list.remove(array[index_to_be_picked])
#     target +=array[index_to_be_picked]
#     combination_sum(array,target,index_to_be_picked+1,final_list,temp_list)


def  combination_sum(array,target,index_to_be_picked,final_list,temp_list):
    """
    Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates
    where the chosen numbers sum to target. You may return the combinations in any order.

    The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
    frequency
    of at least one of the chosen numbers is different.

    The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for 
    the given input.
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]

    """
    # print("holla")
    # print(index_to_be_picked,target,final_list,temp_list,"start_print")
    
    if index_to_be_picked>=len(array)-1:
        if target==0:
            print(temp_list,"**********************")
        return

    elif(array[index_to_be_picked]<=target):
        target -=array[index_to_be_picked]
        temp_list.append(array[index_to_be_picked])
        combination_sum(array,target,index_to_be_picked,final_list,temp_list)
        target += array[index_to_be_picked]
        # print(temp_list,"temp_list",target)
        temp_list.pop()
    combination_sum(array,target,index_to_be_picked+1,final_list,temp_list)
            
    #         combination_sum(array,target,index_to_be_picked+1,final_list,temp_list)
    # elif index_to_be_picked<len(array)-1:
    #     if array[index_to_be_picked]>target:
    #         return
    #     else:
    #         target -=array[index_to_be_picked]
    #         temp_list.append(array[index_to_be_picked])
    #         combination_sum(array,target,index_to_be_picked,final_list,temp_list)
    #         target += array[index_to_be_picked]
    #         # print(temp_list,"temp_list",target)
    #         temp_list=temp_list[:-1]#.pop()
            
    #         combination_sum(array,target,index_to_be_picked+1,final_list,temp_list)

def main():
    array =[2,3,5,7]
    target = 7
    index_to_be_picked= 0
    print("start")
    print("The sorted array is",combination_sum(array,target,index_to_be_picked,[],[]))

if __name__=="__main__":
    main()  #/mnt/d/programming/CODE/Subsequences.py

    