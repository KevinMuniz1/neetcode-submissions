class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        oneDArray = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                oneDArray.append(matrix[i][j])
        print(oneDArray)
        
        l = 0
        r = len(oneDArray) -1

        while l <= r:
            mid = l + (r-l) // 2
            if oneDArray[mid] > target:
                r = mid - 1
            elif oneDArray[mid] < target:
                l = mid + 1
            else:
                return True
        return False
                

        