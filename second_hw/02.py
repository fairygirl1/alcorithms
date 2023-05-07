class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 1:
            return 0
        
        nums = [None for i in range(n + 1)]
       #нужно пройтись по всем элементам списка nums
        
        nums[0] = 0
        nums[1] = 1
        
        for i in range(0, n + 1):
	# если индекс 2 * i, то nums[2 * i] получает значение nums[i]
            if 2 <= 2 * i <= n:
                nums[2 * i] = nums[i]
            
        # если индекс 2 * i + 1, то nums[2 * i + 1] получает значение nums[i] + nums[i + 1]
            if 2 <= 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
        
        return max(nums)
	# возвращает максимальное значение в последовательности, которое соответствует максимальному элементу в списке nums.
        #O(n)
