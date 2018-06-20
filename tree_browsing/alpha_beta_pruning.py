def alpha_beta_pruning(node, depth, alfa = float('-inf'), beta= float('inf'), maximizingPlayer = True):
    #pseudo-code here : https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
    #alfa : minimum score that maximizing is assured
    #beta : maximum score that minimizing is assured
    if len(node.children) == 0:
        return node.value
    if maximizingPlayer is True:
        v = float('-inf')
        for child in node.children:
            v = max(v, alpha_beta_pruning(child, depth-1, alfa, beta, False))
            alfa = max(alfa, v)
            if beta <= alfa:
                break
        return v
    else:
        v = float('inf')
        for child in node.children:
            v = min(v, alpha_beta_pruning(child, depth-1, alfa, beta, True))
            beta = min(beta, v)
            if beta <= alfa:
                break
        return v

def alpha_beta_wrapper(tree , maximazingPlayer : bool):
    return [alpha_beta_pruning(node=node, depth=len(tree.levels), maximizingPlayer =maximazingPlayer) for node in tree.levels[0]]

