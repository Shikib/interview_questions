def quickselect(arr, k):
  if len(arr) == 1:
    return arr[0]

  pivot = arr[0]
  left = [e for e in arr if e < pivot]
  right = [e for e in arr if e > pivot]
  if k <= len(left):
    return quickselect(left, k)
  elif k == len(left) + 1:
    return pivot
  else:
    return quickselect(right, k - len(left) - 1)

def smallest_k(arr, k):
  kth_small = quickselect(arr, k)
  ret = []
  for e in arr:
    if e <= kth_small:
      ret.append(e)
  return ret

  #return [e for e in arr if e <= kth_small]
