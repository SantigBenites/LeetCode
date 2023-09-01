def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # nums = [0,_,1,1,1,2,2,3,3,4]
    #           i
    #         j
    # set = {0} 
    seenNums = set()
    j = 0

    for i in range(0,len(nums)):
        
        if nums[i] not in seenNums:
            seenNums.add(nums[i])
            
        else:
            nums[i] = "_"
            if nums[i-1] != "_":
                j = i
            

    return nums
        

nums = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums))