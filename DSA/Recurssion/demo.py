# def check(nums):
#     flag=0
#     if len(nums)>2:
#         if nums[0]>nums[len(nums)-1]:
#             flag=0
#         else:
#             flag=1
#     print(flag,"===")
#     for i in range(len(nums)//2):
#         if flag:
#             if nums[i]<nums[len(nums)-i-1]:
#                 print(i,"--",len(nums)-i-1)
#                 continue
#             else:
#                 return False
#         else:
#             if nums[i]>nums[len(nums)-i-1]:
#                 continue
#             else:
#                 return False
#     return True
# print(check([9,12,20,88,46,52]))

# def removeDuplicates( nums):
#     answer_list=[]
#     for i in range(len(nums)):
#         if nums[i] not in answer_list:
#             answer_list.append(nums[i])
#     print(answer_list)
#     return len(answer_list)

# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

# a=[1,2,3]
# b=[4,5,6]
# print(a[:2])
# print(b[2:])
# print(a[:]+b[:])
import copy

def check( nums) :

    length_Array=len(nums)
    array = copy.deepcopy(nums)
    for element in range(length_Array):
        for j in range(element,0,-1):
            if (array[j]< array[j-1])&(j-1>=0):
                array[j],array[j-1] = array[j-1],array[j]

    maximum_elemnt=[0]
    pointer=0
    for i in range(1,length_Array):
        if nums[i]>=nums[maximum_elemnt[pointer]]:
            maximum_elemnt.append(i)
            pointer+=1
    if len(maximum_elemnt)==1:
        rotation_right =length_Array-maximum_elemnt-1
        new_array_roated = nums[maximum_elemnt[0]+1:]+nums[:maximum_elemnt[0]+1]
    else:
        new_array_roated = nums[maximum_elemnt[0]+1:]+nums[:maximum_elemnt[0]+1]
        oyo = len(new_array_roated)
        print(maximum_elemnt,"maximum==")
        for i in maximum_elemnt:
            new_array_roated[oyo] = nums[i]
            oyo+=1

    if new_array_roated==array:
        return True
    else:
        return False

check([6,7,7,5])