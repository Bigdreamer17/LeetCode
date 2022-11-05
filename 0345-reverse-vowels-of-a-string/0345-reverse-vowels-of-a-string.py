class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        vowel = ['a', 'e', 'i', 'o','u']
        stack = list(s)
        
        while l < r:
            if stack[l].lower() in vowel and stack[r].lower() in vowel:
                stack[l], stack[r] = stack[r], stack[l]
                l += 1
                r -= 1
            elif stack[l].lower() in vowel or stack[r].lower() not in vowel:
                r -= 1
            elif stack[l].lower() not in vowel or stack[r].lower() in vowel:
                l += 1
        return "".join(stack)
        