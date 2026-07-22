class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        for current_bracket in s:
            if current_bracket in ["(", "{", "["]:
                brackets.append(current_bracket)
            else:
                previous_bracket = brackets[-1] if brackets else None

                # not matching, so entire string s in invalid, returns early
                if (
                    (current_bracket == "(" and previous_bracket != ")")
                    or (current_bracket == "{" and previous_bracket != "}")
                    or (current_bracket == "[" and previous_bracket != "]")
                ):
                    return False

                # there's a matching closing bracket, so removed it
                brackets.pop()

        # if all matched, then there should be anything in brackets
        return len(brackets) == 0
