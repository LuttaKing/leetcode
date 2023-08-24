'''Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.'''

def sumOfTwo(nums:list, target: int):

    for n in nums:
        
        differnce = target-n
        if differnce in nums:
            

            print(f'found {differnce, n} on indexes {nums.index(n),nums.index(differnce)}')
           
            break




# sumOfTwo([2,11,6,3,1,4,5] ,9)
sumOfTwo([3,3],6)

      