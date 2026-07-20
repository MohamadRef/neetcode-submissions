from collections import defaultdict # must include
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list) # using the hashmap
        
        for s in strs:
            sorted_s = tuple(sorted(s))  # sorted characters as the key, tuple so it become immutable aray
            #so like a c t , will have act and cat , etc...
            #each letter here is the key and the word is its value 
            anagram_map[sorted_s].append(s)  # group anagrams by key
        
        return list(anagram_map.values())  # return list of grouped anagrams
