class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1

        def sort_key(item):
            # item is a tuple: (word, count)
            # Return a tuple: (-count, word)
            return (-item[1], item[0])

        sorted_words = sorted(freq.items(), key=sort_key)

        return [word for word, count in sorted_words[:k]]