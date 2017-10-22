from collections import defaultdict

def group_anagrams(arr):
  groups = defaultdict(list)
  for e in arr:
    groups["".join(sorted(e))].append(e)

  return list(groups.values())
