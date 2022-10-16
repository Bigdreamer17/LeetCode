class Solution:
    def sortSentence(self, s: str) -> str:
        txt = sorted(s.split(), key=lambda t:t[-1], reverse = False)
        return " ".join([t[:-1] for t in txt])