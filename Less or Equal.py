class solution:
    def less_or_equal(self, n, k, nums: list[int]):
        nums = nums.sorted()
        if k == 0:
            if nums[0] ==  1:
                return -1
            else :
                return 1
        else :
            if nums[k-1] == nums[k]:
                return -1
            else :
                return nums[k-1]
