class Solution:
    def trap(self, h: List[int]) -> int:
        l, r = 0, len(h) - 1 
        lmax, rmax = h[l], h[r]

        res = 0

        while l < r:
            if lmax <= rmax:
                l += 1
                lmax = max(lmax, h[l])
                res += lmax - h[l]
            else:
                r -= 1
                rmax = max(rmax, h[r])
                res += rmax - h[r]

        return res
