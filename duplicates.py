def duplicate(arr):
  s = set()
  for e in arr:
    if e in s:
      return True
    s.add(e)

  return False
