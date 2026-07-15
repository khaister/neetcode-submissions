class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            # ignore non-alphanumeric values
            if not s[i].isalnum():
                i += 1
            if not s[j].isalnum():
                j -= 1

            # if at least one pair not matching, 
            # then not a valid palindrome,
            # so no need to check the rest
            if s[i].lower() != s[j].lower():
                print(s[i], s[j])
                return False

            i += 1
            j -= 1

        # all letter pairs match, so must be a palindrome
        return True