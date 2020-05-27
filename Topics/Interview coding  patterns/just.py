def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  x = 0
  results = {}
  temp = []
  n = len(arr)
  while x < n:
    temp.append(arr[x])
    if len(temp) == k:
      results[sum(temp)] = temp
      temp = [arr[x]]
    x+=1
  max_k = max(list(results.keys()))
  for k, v in results.items():
    if k == max_k:
      return v
  return -1
print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))