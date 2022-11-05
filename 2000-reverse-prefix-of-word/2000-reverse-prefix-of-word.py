class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Looping through the range of the string
        for i in range(len(word)):
            # Check if our current character is equal to ch
            if word[i] == ch:
                # If so return the reversed characters plus the characters after it 
                return word[:i+1][::-1] + word[i+1:]
        # Else if you cab't find the ch character return the word itself
        return word 
        