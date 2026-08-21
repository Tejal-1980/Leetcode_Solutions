class Solution:
    def NthRoot(self, n, m):
        low=1
        high=m
        while low<=high:
            mid=(low+high)//2
            value=1
            for _ in range(n):
                value*=mid
                if value > m:
                    break
            if value==m:
                return mid
            elif value > m:
                high=mid-1
            else:
                low=mid+1
        return -1

      