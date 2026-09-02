class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """

        n = len(bloomDay)

        # Not enough flowers
        if m * k > n:
            return -1

        low = min(bloomDay)
        high = max(bloomDay)

        result = -1

        while low <= high:
            mid = (low + high) // 2

            bouquets = 0
            flowers = 0

            for day in bloomDay:
                if day <= mid:
                    flowers += 1

                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            if bouquets >= m:
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result