def num_subgraph(nodes):
  """
  node: (id, neighbors)
  """
  seen = {}
  def _dfs(cur): 
    if cur.id in seen:
      return 0

    for n in cur.neighbors:
      _dfs(n)

    return 0

  count = 0
  for v in nodes:
    if v.id not in seen:
      count += 1
      _dfs(v)

  return count
