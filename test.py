from games.connect4 import Connect4, heuristics_c4
import tree.treeStructure
import time
import tree_browsing.alpha_beta_pruning

"""

tree = tr.tree()
list_node = [tr.tree_node(value=i, parent_abs_id=-10) for i in range(1)]
tree.add_level(list_tree_node=list_node)


list_node2 = [tr.tree_node(value=i*2, parent_lvl_id=int(i/2)) for i in range(2)]
tree.add_level(list_tree_node=list_node2)
values = [5, 6, 7, 4]
list3 = [tr.tree_node(value=values[i], parent_lvl_id=int(i/2)) for i in range(4)]
tree.add_level(list_tree_node=list3)

print(tree)

print(minimax.minimax_wrapper(tree, True))
"""







"""
start = time.time()

p4 = Connect4.Connect4(n=6, m=7)
heur = heuristics_c4.heuristics_c4()
tree = tree.treeStructure.Tree(depth=5, heuristics=heur)
tree.build_tree(p4)
print(tree_browsing.alpha_beta_pruning.alpha_beta_wrapper(tree, False))

end = time.time()
print('Total time:', end - start)
"""

p4 = Connect4.Connect4(n=6, m=7)
heur = heuristics_c4.heuristics_c4()

p4.board[4][3] = 'O'
p4.board[3][3] = 'O'
p4.board[2][3] = 'O'
p4.board[1][3] = 'O'

print(heur.generate_score(game_state=p4))
print(p4)
