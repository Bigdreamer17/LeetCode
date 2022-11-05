class Solution:
    def reverseVowels(self, s: str) -> str:
        # Initialize Two pointers first(l) on second(r) on the end of string
        l = 0
        r = len(s) - 1
        # saving the vowels in one list
        vowel = ['a', 'e', 'i', 'o','u']
        # Changing the string to list so we can operate on it
        stack = list(s)
        
        while l < r:
            # Checking if the lowercase of the l pointer value and r pointer value are vowels
            if stack[l].lower() in vowel and stack[r].lower() in vowel:
                #If so swap there place and increment the left pointer and decrement r pointer
                stack[l], stack[r] = stack[r], stack[l]
                l += 1
                r -= 1
                # If the l pointer value is vowel but r pointer value is not
            elif stack[l].lower() in vowel or stack[r].lower() not in vowel:
                # Then decrement the r pointer
                r -= 1
                # If the l pointer value is not vowel but r pointer value is
            elif stack[l].lower() not in vowel or stack[r].lower() in vowel:
                # Then increment the l pointer
                l += 1
            # Return the stack after joinning it 
        return "".join(stack)
        