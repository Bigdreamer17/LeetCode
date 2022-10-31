class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort() # increasing order
        for p1 in range(len(arr)):
            for p2 in range(len(arr)):
                if p2 != p1:
                    if arr[p2] == arr[p1] * 2:
                        return True
                    elif arr[p2] > arr[p1] * 2:
                        break
        return False
        """
        i  = 0 
        r = 1
        test = False
        
        while not test and r < len(arr):
            if arr[i] == arr[r] * 2 or arr[r] == arr[i] * 2:
                test =True
            elif i == r-1:
                r += 1
            elif arr[i] < 0 and arr[i] = 0 and arr[r] > arr[i] * 2:
                i += 1
            else:
                r += 1
        return test """