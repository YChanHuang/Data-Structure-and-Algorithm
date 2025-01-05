from typing import List
def recursive_sum(lst: List):
    if lst == []:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])

## 
print(recursive_sum([4, 4, 5, 6]))