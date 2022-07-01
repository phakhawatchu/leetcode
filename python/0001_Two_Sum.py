from typing import List

class Solution:
    
    # Less Memory Method
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for self.i in range(len(nums)):
            try:
                self.j = nums.index(target - nums[self.i], self.i+1)
                if (self.j != self.i):
                    return [self.i, self.j]
            except:
                pass

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))