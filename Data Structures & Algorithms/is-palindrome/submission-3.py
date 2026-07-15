class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            # ignore non-alphanumeric values
            if i < j and not (s[i] and s[i].isalnum()):
                i += 1
                continue
            if i < j and not (s[j] and s[j].isalnum()):
                j -= 1
                continue

            # if at least one pair not matching, 
            # then not a valid palindrome,
            # so no need to check the rest
            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        # all letter pairs match, so must be a palindrome
        return True