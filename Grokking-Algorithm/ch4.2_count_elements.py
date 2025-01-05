def my_count(lst):
    if lst == []:
        return 0
    else:
        return 1 + my_count(lst[1:])


print(my_count([1, 3, 5, 6, 0]))