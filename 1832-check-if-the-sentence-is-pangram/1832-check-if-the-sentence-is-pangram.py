class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        word_count = {}
        for i in sentence:
            word_count[i] = 1 + word_count.get(i, 0)
        if len(word_count) >= 26:
            return True
        else:
            return False