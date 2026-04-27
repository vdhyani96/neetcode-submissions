class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        longest_seq = 0
        for num in hashset:
            if num-1 in hashset:
                continue
            nextval = num + 1
            cur_len = 1
            while nextval in hashset:
                cur_len += 1
                nextval += 1
            longest_seq = max(cur_len, longest_seq)
        return longest_seq