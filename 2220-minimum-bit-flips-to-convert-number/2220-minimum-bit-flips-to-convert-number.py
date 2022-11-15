class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # bit_diff helps us find how many bits are diffeent
        bit_diff = start ^ goal
        count = 0
        while bit_diff:
            # helps us calculate the number of 1's in a number
            bit_diff &= bit_diff - 1
            
            count += 1
        return count 