from tree import treeStructure as tr
import random

def generate_random_tree(nb_levels : int, nb_children : int):
    print('Number of nodes :', sum([nb_children**i for i in range(1, nb_levels+1)]))
    tree = tr.Tree(depth=nb_levels, heuristics=None)
    for i in range(nb_levels):
        tree.add_level([tr.TreeNode(value=random.uniform(-100, 100), parent_lvl_id=int(a / nb_children)) for a in range(nb_children ** (i + 1))])
    return tree