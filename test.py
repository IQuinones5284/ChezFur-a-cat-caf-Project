def twoSum(nums, target): 
    numStorage = dict()
    for index, num in enumerate(nums):
        complement = target - num 
        if complement in numStorage: 
            return numStorage[complement], index
        else:
            numStorage[num] = index

print(twoSum([2,7,8,9,7,6], 9))
