class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Intiating Two pointers one at the front(l) and one at the back(r)
        l = 0 
        r = len(s) - 1
        
        
        while l < r:
            # Check if s[l] or s[l] is either alphabet or number if not move pointers
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
                
            else:
                #Check the lower part  of s[l] or s[r] are not equal if so return False  
                if s[l].lower() != s[r].lower():
                    return False
                # Otherwise Increment l, decrement r and return True
                else:
                    l += 1
                    r -= 1 
        return True 
                
                