# Write a recursive function to find the maximum number in a list.

def my_max(list):
  if len(list) == 2:
    return list[0] if list[0] > list[1] else list[1]
  sub_max = my_max(list[1:])
  return list[0] if list[0] > sub_max else sub_max


