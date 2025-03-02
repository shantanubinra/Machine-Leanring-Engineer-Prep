# nums=[6,7,7,5]
# maximum_elemnt=0
# length_Array=len(nums)
# for i in range(1,length_Array):
#     print(nums[i],"--",i)
#     if nums[i]>nums[maximum_elemnt]:
#         maximum_elemnt =i
# print("================")
# print(maximum_elemnt)

# def sumOfSeries(n):
#     #code here
#     if n==1:
#         return 1
#     c=sumOfSeries(n)^3+ sumOfSeries(n-1)^3
#     n=n-1

# def sumOfSeries(n):
#         #code here
#         print(n)
#         if n==1:
#             return 1
#         return (n*n*n)+ sumOfSeries(n-1)^3

# print(sumOfSeries(2))
k=2
nums=[-1,-100,3,99]
# nums = nums[]]+nums[]
# print(nums)
length =len(nums)
# for term in range(k):

temp_variable = nums[length-1-k:]
for i in range(length-1-k,0,-1):
    nums[i]=nums[i-1]
nums[:k]=temp_variable
print(nums)