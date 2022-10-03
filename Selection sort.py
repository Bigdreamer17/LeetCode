class Solution: 
    def selectionSort(self, arr,n):
        #code here
        for s in range(len(arr)):
            min_ind = s
            
            for i in range(s + 1,len(arr)):
                
                if arr[i] < arr[min_ind]:
                    min_ind = i
            arr[s], arr[min_ind] = arr[min_ind], arr[s]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends