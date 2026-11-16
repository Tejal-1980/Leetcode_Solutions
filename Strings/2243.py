class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        while len(s) > k:

            result = []

            for i in range(0, len(s), k):

                group = s[i:i+k]

                total = sum(int(ch) for ch in group)

                result.append(str(total))

            s = ''.join(result)

        return s
        