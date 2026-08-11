class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        print(s)
        strs = [] 
        i = 0

        while i < len(s):
            _s = ""
            l = ""
            while s[i] != "#":
                l += s[i]
                i += 1

            i += 1
            print(l)
            l = int(l)

            while l:
                _s += s[i]
                i += 1
                l -= 1

            strs.append(_s)

        return strs
