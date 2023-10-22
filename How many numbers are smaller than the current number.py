class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)
        dict = {}
        res = []
        for i in range (len(sorted_num)):
            if sorted_num[i] not in dict:
                dict[sorted_num[i]] = i
        
        for i in nums:
            res.append(dict[i])
        return res        
