def power_set(arr):
  pset = [ [] ]
  for e in arr:
    n_pset = []
    for s in pset:
      n_pset.append(s + [e])

    pset += n_pset

  return pset
