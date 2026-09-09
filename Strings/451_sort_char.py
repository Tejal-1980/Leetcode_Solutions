class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}

        # Count frequency of each character
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Sort characters by frequency (highest first)
        chars = sorted(freq, key=freq.get, reverse=True)

        # Create result
        result = ""

        for ch in chars:
            result += ch * freq[ch]

        return result