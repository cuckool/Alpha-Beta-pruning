def negamax_alpha_beta(node, depth, alpha, beta, color):
    """
    Initial call for Player A's root node
    rootNegamaxValue := negamax( rootNode, depth, −∞, +∞, 1)

    :param node:
    :param depth:
    :param alpha:
    :param beta:
    :param color: if maximizing player : 1 || if minimizing player : -1
    :return:
    """
    if depth == 0 or len(node.children) == 0:
        return node.value
    best_value = float('-inf')
    for child in node.children:
        v = -negamax_alpha_beta(child, depth-1, -beta, -alpha, -color)
        best_value = max(best_value, v)
        alpha = max(alpha, v)
        if alpha >= beta:
            break
    return best_value

def negamax_alpha_beta_wrapper(tree, maximizing_player):
    return [negamax_alpha_beta(node=node, depth=len(tree.levels), alpha=float('-inf'), beta=float('inf'), color=maximizing_player) for node in tree.levels[0]]