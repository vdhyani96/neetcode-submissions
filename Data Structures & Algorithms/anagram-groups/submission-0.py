class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            sorted_key = "".join(sorted(word))
            if sorted_key in hashmap:
                hashmap[sorted_key].append(word)
            else:
                hashmap[sorted_key] = [word]
        
        return list(hashmap.values())

