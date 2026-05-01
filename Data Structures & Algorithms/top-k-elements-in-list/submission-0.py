class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using heap will give us time O(klogn)
        from collections import Counter
        import heapq
        counter = Counter(nums)

        heap = []
        for num, freq in counter.items():
            heapq.heappush(heap,(freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for freq, num in heap]