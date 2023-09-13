'''Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.'''

def sumOfTwo(nums:list, target: int):
    seen={}

    for index,num in enumerate( nums):
        diff = target - num
        if diff in seen: # diff/key in {}
            print(f'{diff} found in {seen}')
            print(f'Found indexes :{nums.index(diff), index}')
        seen[num]=index #add to dict
        print(seen)

# sumOfTwo([2,11,6,3,1,4,5] ,9)
sumOfTwo([3,3],6)

      