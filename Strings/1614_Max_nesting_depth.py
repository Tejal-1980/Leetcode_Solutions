class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        count=0
        for ch in s:
            if ch=="(":
                count+=1
                ans=max(ans,count)
                if ch==")":
                    count-=1
        return ans
        