class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        new_list = Counter(arr)
        size = len(arr)
        count = 0
        answer = 0
        for i,j in sorted(new_list.items(), key=lambda x: -x[1]):
            count += j
            answer +=1
            if count >= (size//2): 
                break
        return answer
        