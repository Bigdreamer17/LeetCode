class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # nested-loop to flip it horizontally 
        for img in image:
            i , j = 0, len(img) - 1
            while i <= j:
                img[i] , img[j] = img[j]^1, img[i]^1
                
                i += 1
                j -= 1
        
        return image 