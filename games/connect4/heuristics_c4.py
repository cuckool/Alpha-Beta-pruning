import games.interfaces
import random

class heuristics_c4(games.interfaces.Heuristics):
    def generate_score(self, game_state: games.interfaces.InterfaceGames2Player):
        if self.check_victory(game_state):
            return self.check_victory(game_state)
        else:
            score_horizontal = self.check_horizontal_strings(game_state, 'X') + self.check_horizontal_strings(game_state, 'O')
            score_vertical = self.check_vertical_string(game_state, 'X') + self.check_vertical_string(game_state, 'O')
            score_diagonale = self.check_diagonal_string(game_state, 'X') + self.check_diagonal_string(game_state, 'O')
            return score_horizontal + score_vertical + score_diagonale + self.reward_middle(game_state)



    def reward_middle(self, game_state: games.interfaces.InterfaceGames2Player):
        score_middle = 0
        for i in range(game_state.n):
            for j in range(int(game_state.m/3), int(game_state.m/3)*2):
                if game_state.board[i][j] == 'O':
                    score_middle -= 1
                elif game_state.board[i][j] == 'X':
                    score_middle += 1
        return score_middle

    def check_horizontal_strings(self, game_state: games.interfaces.InterfaceGames2Player, jeton : str ):
        score_string = 0
        for i in range(game_state.n):
            for j in range(game_state.m-1):
                ref = game_state.board[i][j]
                if (ref == jeton):
                    string_size = 1
                    for k in range(1,game_state.m-j):
                        if game_state.board[i][j+k] == ref:
                            string_size += 1
                        else:
                            break
                    if string_size > 1:
                        if jeton == 'X':
                            score_string += string_size * 10
                        else:
                            score_string -= string_size * 10
        return score_string

    def check_vertical_string(self, game_state: games.interfaces.InterfaceGames2Player, jeton : str ):
        score_string = 0
        for i in range(game_state.n-1):
            for j in range(game_state.m):
                ref = game_state.board[i][j]
                if (ref == jeton):
                    string_size = 1
                    for k in range(1, game_state.n - i):
                        if game_state.board[i+k][j] == ref:
                            string_size += 1
                        else:
                            break
                    if string_size > 1:
                        if jeton == 'X':
                            score_string += string_size * 10
                        else:
                            score_string -= string_size * 10
        return score_string

    def check_diagonal_string(self, game_state: games.interfaces.InterfaceGames2Player, jeton : str):
        score_string = 0
        for i in range(game_state.n-1):
            for j in range(game_state.m):
                ref = game_state.board[i][j]
                if ref == jeton:
                    string_size = 1
                    borne_max = min(game_state.n-i, game_state.m-j)

                    for k in range(1,borne_max):
                        if game_state.board[i+k][j+k] == ref:
                            string_size += 1
                        else:
                            break

                    if j < game_state.n-i:
                        borne_max = j+1
                    else:
                        borne_max = game_state.n-i
                    for l in range(1,borne_max):
                        if game_state.board[i+l][j-l] == ref:
                            string_size += 1
                        else:
                            break
                    if string_size > 1:
                        if jeton == 'O':
                            score_string -= string_size * 10
                        else:
                            score_string += string_size * 10
        return score_string



    def check_victory(self,  game_state: games.interfaces.InterfaceGames2Player):
        for i in range(game_state.n-1):
            for j in range(game_state.m):
                ref = game_state.board[i][j]
                if ref != '_':
                    string_size = 1
                    for k in range(1, game_state.n - i):
                        if game_state.board[i+k][j] == ref:
                            string_size += 1
                        else:
                            break
                    if string_size >= 4:
                        if ref == 'X':
                            return float('inf')
                        else:
                            return float('-inf')

        for i in range(game_state.n):
            for j in range(game_state.m-1):
                ref = game_state.board[i][j]
                if ref != '_':
                    string_size = 1
                    for k in range(1,game_state.m-j):
                        if game_state.board[i][j+k] == ref:
                            string_size += 1
                        else:
                            break
                    if string_size >= 4:
                        if ref == 'X':
                            return float('inf')
                        else:
                            return float('-inf')
        for i in range(game_state.n-1):
            for j in range(game_state.m):
                ref = game_state.board[i][j]
                if ref != '_':
                    string_size = 1
                    borne_max = min(game_state.n-i, game_state.m-j)

                    for k in range(1,borne_max):
                        if game_state.board[i+k][j+k] == ref:
                            string_size += 1
                        else:
                            break
                    if string_size >= 4:
                        if ref == 'O':
                            return float('-inf')
                        else:
                            return float('inf')

                    string_size = 1
                    if j < game_state.n-i:
                        borne_max = j+1
                    else:
                        borne_max = game_state.n-i
                    for l in range(1,borne_max):
                        if game_state.board[i+k][j-k] == ref:
                            string_size += 1
                        else:
                            break
                    if string_size >= 4:
                        if ref == 'O':
                            return float('-inf')
                        else:
                            return float('inf')