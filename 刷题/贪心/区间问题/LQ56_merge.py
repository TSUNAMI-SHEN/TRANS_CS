class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0: return intervals
        intervals.sort(key=lambda x:x[0])   # 需要先排序
        result = []
        result.append(intervals[0])
        
        for i in range(1, len(intervals)):
            last = result[-1]
            if last[1] >= intervals[i][0]:   # 如果有重叠，则选取覆盖最远的右边界
                result[-1] = [last[0], max(last[1], intervals[i][1])]
            else:
                result.append(intervals[i])
        return result
