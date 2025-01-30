# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

    for i in range(len(nums)):
        idx = i
        for j in range(i+1,len(nums)):
            if nums[idx] > nums[j]:
                idx = j
    
        nums[i],nums[idx] = nums[idx],nums[i]

    return nums