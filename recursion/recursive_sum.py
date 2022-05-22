def sum(list):
  if list == []:
    return 0
  return list[0] + sum(list[1:])

list = [2, 10, 30, 4]
print(sum(list))