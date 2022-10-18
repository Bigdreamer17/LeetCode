class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        
        mi = []
        curr = 0
        for t in trips:
            numpass,s,e = t
            while mi and mi[0][0] <= s:
                curr -= mi[0][1]
                heapq.heappop(mi)
                
            curr += numpass
            if curr > capacity:
                return False
            heapq.heappush(mi, [e,numpass])
        return True 