from typing import List

def read_integers() -> List[int]:

    numList = input().split(",")
    
    return [int(x) for x in numList]
        

    
    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
