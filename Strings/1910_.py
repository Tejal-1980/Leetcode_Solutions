class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        stack=[]
        n=len(part)
        for ch in s:
            stack.append(ch)
            if len(stack)>=n and "".join(stack[-n:])==part:
                for _ in range(n):
                    stack.pop()
        return "".join(stack) 

            
               

         
            
                
            



             
        