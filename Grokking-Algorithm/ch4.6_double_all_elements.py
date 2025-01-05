def double_each_element(lst):
    if lst == []:
        return []
    else:
        return [lst[0] * 2] + double_each_element(lst[1:])
        
print(double_each_element([1, 3, 5]))

