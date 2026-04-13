class Solution:
    def sortColors(self, numbers: List[int]) -> List[int]:
        count = [0] * 3
        
        for n in numbers:
            count[n] +=1
    
        index = 0
        for i in range(len(count)):
            while count[i]:
                count[i] -= 1
                numbers[index] = i
                index += 1
