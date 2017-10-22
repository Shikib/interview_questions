def is_bipartite(G):
    """
    G is a mapping from id -> node

    { 0: node1, 1: node2, 2 : node3 }

    node.id, node.neighbors
    """
    white_nodes = set()
    black_nodes = set()
    
    def _dfs(node, colour):
        """
        node is a node
        colour is white/black
        """
        if ((node.id in white_nodes and colour == "black") or
            (node.id in black_nodes and colour == "white")):
            return False
        
        if node.id in white_nodes or node.id in black_nodes:
            return True
        
        if colour == "black":
            black_nodes.add(node.id)
        else:
            white_nodes.add(node.id)
        
        for neighbor_id in node.edges:
            ret_val = _dfs(G[neighbor_id], "white" if colour == "black" else "black")
            if not ret_val:
                return False
        
        return True
    
    #for node in G.values():
    #    if node.id not in white_nodes and node.id not in black_nodes:
    #        val = _dfs(node, "white")
    #        if not val:
    #            return False
            
    return _dfs(node, "white")
