def minimax(node, depth, maximizingPlayer):
    if len(node.children) == 0:
        return node.value
    if maximizingPlayer is True:
        bestValue = float('-inf')
        for child in node.children:
            v = minimax(child, depth - 1, False)
            bestValue = max(bestValue, v)
        return bestValue
    else:
        bestValue = float('inf')
        for child in node.children:
            v = minimax(child, depth - 1, True)
            bestValue = min(bestValue, v)
        return bestValue


def minimax_wrapper(tree, maximizingPlayer : bool):
    return [minimax(node=node, depth=len(tree.levels), maximizingPlayer =maximizingPlayer) for node in tree.levels[0]]