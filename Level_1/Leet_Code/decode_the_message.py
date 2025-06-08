class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        table = {}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        idx = 0

        # Create a map of characters from key to alphabet
        # E.g. table = {'a': 't', 'b': 'h', 'c': 'e', ...}
        for char in key:
            if char != ' ' and char not in table: # Only check not-found charcters
                table[char] = alphabet[idx]
                idx += 1
                if idx == 26:
                    break # Gone through all letters of the alphabet

        # Decode the message
        decoded = []
        for char in message:
            if char == ' ':
                decoded.append(' ')
            else:
                decoded.append(table[char]) # Fetch the character from the table
        return ''.join(decoded)