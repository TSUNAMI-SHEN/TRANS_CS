class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # 利用哈希表
        hashtable = dict()

        for i in range(len(nums)):
            if target - nums[i] in hashtable:
                return [hashtable[target-nums[i]], i]
            hashtable[nums[i]] = i
        return []
