class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # key -> set; key is the letters for a given anagram group sorted in alphabetical order
        for word in strs:
            key = self.build_key(word)
            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)
        
        return [list(g) for g in groups.values()]

    def build_key(self, word: str) -> tuple:
        count = [0] * 26
        for letter in word:
            count[ord(letter) - ord('a')] += 1
        return tuple(count)