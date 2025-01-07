def my_max(lst):
    if len(lst) == 1:
        return lst[0]  # Base case: If there's only one element, return it
    else:
        max_of_rest = my_max(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest


print(my_max([1, 6, 99, 10, 333, 666, 7777, 2, 4, 6]))])

