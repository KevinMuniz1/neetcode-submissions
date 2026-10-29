from typing import List

def find_current_max(arr: List[int]) -> int:
    maxVal = arr[0]
    for num in arr:
        maxVal = max(maxVal,num)
    
    return maxVal


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    res = []
    for numList in nested_arr:
        res.append(find_current_max(numList))
    
    return res
        
    


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
