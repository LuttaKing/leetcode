'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true

'''
numz = range(1,3000000)
def containsDuplicate( nums) -> bool:
        lis=[] 
              
        for num in nums:
            if num in lis:
                  return True
            else: 
                  lis.append(num)
        return False
                  
        
print(containsDuplicate(numz))

# def containsDuplicateUsingSet( nums) -> bool:
# # set returns unique dict
#         if len(set(nums)) == len(nums):
#               return False
#         else:
#               return True
# print(containsDuplicateUsingSet(numz))

