class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = {}
        # Now we know they are the same length
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]] += 1
            if t[i] not in hashmap:
                hashmap[t[i]] = -1
            else:
                hashmap[t[i]] -= 1
        
        # after the loop above, all values should be 0
        for val in hashmap.values():
            if val != 0:
                return False
        return True