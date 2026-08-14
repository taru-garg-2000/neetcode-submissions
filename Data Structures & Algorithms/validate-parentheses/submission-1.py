class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for c in s:
            if c == "[" or c == "(" or c == "{":
                st.append(c)
            elif c in ["]", "}", ")"] and len(st) == 0:
                return False
            elif c in ["]", "}", ")"]:
                if (c == "]" and st[-1] == "[") or (c == "}" and st[-1] == "{") or (c == ")" and st[-1] == "("):
                    st.pop()
                else:
                    return False
            else:
                return False


        return len(st) == 0