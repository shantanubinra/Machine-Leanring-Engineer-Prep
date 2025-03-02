#https://leetcode.com/problems/combination-sum-ii/


# def Combination_sum2(array,target,temp_array):
#     """
#     Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates 
#     where the candidate numbers sum to target.
#     Each number in candidates may only be used once in the combination.
#     Note: The solution set must not contain duplicate combinations.

#     """

class Solution:

    def called_function(self,candidates,target,new_array,current_index,final_list):
        print(candidates,target,new_array,current_index,final_list)
        if current_index==len(candidates):
            print("indexwa full hogya")
            if target==0:
                print(new_array,"--------------------------")
                final_list.append(new_array)
                return final_list
            return 
        
        if candidates[current_index]<=target:
            new_array.append(candidates[current_index])
            self.called_function(candidates,target-candidates[current_index],new_array,current_index,final_list)
            new_array.pop()
            # new_array.remove(candidates[current_index])
        self.called_function(candidates,target,new_array,current_index+1,final_list)

        # return final_list

    def combinationSum(self, candidates, target):
        print("combination")
        final_list=[]
        print(candidates,target,"========")
        return self.called_function(candidates,target,[],0,[])
    
def main():
    object1=Solution()
    print(object1.combinationSum([2,3,6,7],7))
    # print("The total number of subsequence",sub_sequence_possible(0,[],[3,2,1]))
    # sub_sequence(0,[],[3,2,1])
    # sub_sequence_sum(0,[],[1,2,1,1,1,3,4],3,0)
    # print(only_one_sub_sequence_sum(0,[],[1,2,1,1,1,3,4],16,0))
    # print(give_count_sub_sequence_sum(0,[],[1,2,1,1,1,3,4],3,0))
if __name__=="__main__":
    main()  #/mnt/d/programming/CODE/Subsequences.py


    


       