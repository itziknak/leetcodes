def findMin( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        if l==1:
            return nums[0]
        elif l==2:
            return min(nums[0],nums[1])
        else:
            l=int(l/2)
            if nums[l]<nums[-1] and nums[l]>nums[0]:
                return nums[0]
            elif nums[l]<nums[-1]:
                if l==1:
                    return min(nums[0],nums[1])
                else:
                    return findMin(nums[0:l])
            else:
                if l==1:
                    return min(nums[0],nums[-1])
                else:
                    return findMin(nums[l:])  
x=findMin([2,3,4,5,1])  
print(x)      
        