# https://practice.geeksforgeeks.org/problems/killing-spree3020/1

# Killing Spree


class Solution:
    def killinSpree (self, n):

        p = lambda n: n*(n+1)*(2*n+1)//6
        
        lo, hi = 0, n+1
        while lo < hi:
            mi = lo+(hi-lo)//2
            if p(mi) > n:
                hi = mi
            else:
                lo = mi+1
                
        return lo-1