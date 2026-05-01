class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 2nd time without heap (Bucket Sort)
        from collections import Counter, defaultdict
        counter = Counter(nums)

        # create a bucket array
        bucket = [[] for _ in range(len(nums)+1)]

        for num,freq in counter.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(nums), -1, -1):
            if bucket[i] is None:
                continue
            j = 0
            while len(res) < k and j < len(bucket[i]):
                res.append(bucket[i][j])
                j += 1
        return res
