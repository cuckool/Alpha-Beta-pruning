import tree_browsing.alpha_beta_pruning
from tree import treeStructure
from games.connect4 import Connect4, heuristics_c4

p4 =Connect4.Connect4(n=6, m=7)
heur = heuristics_c4.heuristics_c4()
while True:
    tree = treeStructure.Tree(depth=5, heuristics=heur)
    tree.build_tree(p4)
    best_moves = tree_browsing.alpha_beta_pruning.alpha_beta_wrapper(tree, True)
    print(best_moves)
    print(best_moves.index(max(best_moves)))
    p4.make_move(column=best_moves.index(max(best_moves)))
    print(p4)
    if heur.check_victory(game_state=p4) == float('inf'):
        print("Computer wins, better luck next time.")
        break
    move = int(input("Your move ? "))
    p4.make_move(column=move)
    print(p4)
    if heur.check_victory(game_state=p4) == float('-inf'):
        print("You win, congratulations.")
        break
    tree = None
