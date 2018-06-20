import games.interfaces

class Connect4(games.interfaces.InterfaceGames2Player):
    def __init__(self, **kwargs):
        self.maximizing_turn_now = True
        self.board = []
        if 'n' in kwargs and 'm' in kwargs:
            self.n = kwargs['n']
            self.m = kwargs['m']
            for i in range(self.n):
                row = []
                for j in range(self.m):
                    row.append('_')
                self.board.append(row)

        if 'father' in kwargs:
            self.n = kwargs['father'].n
            self.m = kwargs['father'].m
            for row in kwargs['father'].board:
                self.board.append(row[:])
            self.maximizing_turn_now = kwargs['father'].maximizing_turn_now
    def __str__(self):
        string = ''
        for row in self.board:
            for token in row:
                string += '|' + token
            string += '|\n'
        for i in range(self.m):
            string += '|' + str(i)
        return string+'|'

    def personal_hash(self):
        tuple_board = tuple(self.board[0])
        for row in self.board[1:]:
            tuple_board = tuple_board + tuple(row)
        return hash(tuple_board)

    def generate_children(self):
        children = []
        for i in range(len(self.board[0])):
            child = Connect4(father=self)
            child.make_move(i)
            children.append(child)
        return children

    def make_move(self, column : int):
        for row in reversed(self.board):
            if row[column] == '_':
                if self.is_maximizing_player_turn_now() is True:
                    row[column] = 'X'
                else:
                    row[column] = 'O'
                break
        self.maximizing_turn_now = not self.maximizing_turn_now


    def is_maximizing_player_turn_now(self):
        return self.maximizing_turn_now