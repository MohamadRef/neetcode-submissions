from collections import defaultdict # must include
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagram = defaultdict(list) # Create a dictionary where missing keys automatically receive [] as their value.

        for word in strs: 
            sorted_word ="".join(sorted(word)) # will join the sorted word
            group_anagram[sorted_word].append(word) # this does the main thing of sorting { "act": " act, cat"}
        return list(group_anagram.values()) # just return the list with its values