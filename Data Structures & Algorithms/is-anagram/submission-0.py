class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if strings of different lengths then not anagram
        if len(s) != len(t):
            return False
        
        s_char_counts = self.count_chars(s)
        t_char_counts = self.count_chars(t)

        # if contain different character sets then not anagram
        if len(s_char_counts.items()) != len(t_char_counts.items()):
            return False
        
        for letter, count in s_char_counts.items():
            if count != t_char_counts.get(letter, 0):
                return False
        
        return True
        
        
    def count_chars(self, s: str) -> dict:
        char_counts = {}
        for c in s:
            if not char_counts.get(c):
                char_counts[c] = 1
            else:
                char_counts[c] = char_counts[c] + 1
        return char_counts