def negamax(node, depth, color):
    """
    Faire gaffe (sur wikipedia) :

Initial call for Player A's root node
rootNegamaxValue := negamax( rootNode, depth, 1)
rootMinimaxValue := rootNegamaxValue

Initial call for Player B's root node
rootNegamaxValue := negamax( rootNode, depth, −1)
rootMinimaxValue := −rootNegamaxValue >>> gaffe au -

    :param node:
    :param depth:
    :param color: if maximizing player : 1 || if minimizing player : -1
    :return:
    """
    if depth == 0 or len(node.children) == 0:
        return node.value
    best_value = float('-inf')
    for child in node.children:
        v = -negamax(child, depth-1, -color)
        best_value = max(best_value, v)
    return best_value

def negamax_wrapper(tree, maximizingPlayer : int):
    return [negamax(node=node, depth=len(tree.levels), color=maximizingPlayer) for node in tree.levels[0]]