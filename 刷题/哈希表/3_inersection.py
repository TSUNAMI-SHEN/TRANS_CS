class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return self.set_intersection(set1, set2)    
    def set_intersection(self, set1, set2):
        if len(set1) > len(set2):
            return self.set_intersection(set2, set1)    # 对长度较小的集合进行遍历，进一步缩短时间
        return [x for x in set1 if x in set2]
