class Tree:
    def __init__(self, depth : int, heuristics):
        self.levels = []                                #the list containing all the levels of the tree, each level is a collection of nodes
        self.number_of_nodes = 0                        #that we will use to give the absolute id
        self.depth = depth
        self.heuristics = heuristics


    def build_tree(self, game_state, depth=-1):
        """Building the tree from a gamestate."""
        if depth == 0:
            return
        elif depth == -1:
            depth=self.depth
        if type(game_state) is not list:
            game_state = [game_state]
        game_state_2 = []
        list_of_nodes = []
        for ind, game in enumerate(game_state):
            children = game.generate_children()
            game_state_2 += children
            for child in children:
                list_of_nodes.append(TreeNode(value=self.heuristics.generate_score(game_state=child), parent_lvl_id=ind))
        self.add_level(list_of_nodes)
        self.build_tree(game_state_2, depth-1)




    def add_level(self, list_tree_node : list, **kwargs):
        for ind, node in enumerate(list_tree_node):
            node.id_absolute = self.number_of_nodes
            self.number_of_nodes += 1
            node.id_level = ind
            node.level = len(self.levels)
            if node.level == 0:
                node.parent_lvl_id = -1
            else:
                self.levels[-1][node.parent_lvl_id].children.append(node)
        self.levels.append(list_tree_node)

    def __str__(self):
        string = ''
        for ind, level in enumerate(self.levels):
            string +=str(ind)+'|'+' '*int(180/len(level))
            for node in level:
                string += str(node.id_level)+' ('+str(node.id_absolute)+')' + ' ['+ str(node.parent_lvl_id) +']' + ' '*int(180/len(level))
            string += '\n'
        return string


class TreeNode:
    def __init__(self, value, **kwargs):
        #if a parameter has -10 value, the value has not been initiated correctly by the tree method, or it's the
        self.id_level = -10                           #id in the level
        self.id_absolute = -10                        #id in the whold tree
        self.level = -10                              #number of the level in the tree that this neuron belongs to (root is 0)
        self.value = value
        self.children = []
        self.parent_lvl_id = kwargs['parent_lvl_id']

