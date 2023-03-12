import os
import numpy as np

class PuzzleConfig:

    def __init__(self):
        self.configuration = True

    def open_file(self, fname):
        if fname == "start":
            with open(os.path.join("game_config", f"{fname}.txt"), 'r') as state_file:
                file_contents = state_file.read()
            text = [list(map(int, line.split())) for line in file_contents.strip().split('\n')[:-1]]
            one_d_arr = [tile for line in text for tile in line]

            return one_d_arr
        else:
            with open(os.path.join("game_config", f"{fname}.txt"), 'r') as state_file:
                file_contents = state_file.read()
            text = [list(map(int, line.split())) for line in file_contents.strip().split('\n')[:-1]]
            one_d_arr = [tile for line in text for tile in line]

            return one_d_arr
    
    def count_unordered_pairs(self, state):
        unordered = 0
        for r in range(8):
            for c in range(r + 1, 9):
                if state[r] > state[c] and state[r] != 0 and state[c] != 0:
                    unordered += 1

        blank_pos = state.index(0)
        row = 3 - blank_pos // 3

        return (unordered + row) % 2
    
    def print_styled(self, pop_n, exp_n, gen_n, max_fs, curr_d, cost, soln_moves):
        print(f'Nodes Popped: {pop_n}')
        print(f'Nodes Expanded: {exp_n}')
        print(f'Nodes Generated: {gen_n}')
        print(f'Max Fringe Size: {max_fs}')
        print(f'Solution found at depth {curr_d} with cost {cost}')
        print("Steps:")
        for move in soln_moves:
            print(f"Move {move[0]} {move[-1]}")

    def track_solution_cost(self, seq):
        solution_moves = []
        solution_cost = 0

        end = True
        curr_idx = 1

        while end:
            curr_idx += 1
            prev_idx = curr_idx - 1

            prev = seq[prev_idx]
            curr = seq[curr_idx]
            empty_tile = np.where(prev[0] == 0)[0][0]
            if (curr[-1])  == "Down":
                cost += curr[0][empty_tile]
                solution_moves.append((curr[0][empty_tile], "Up"))
            if (curr[-1]) == "Up":
                cost += curr[0][empty_tile]
                solution_moves.append((curr[0][empty_tile], "Down"))
            if (curr[-1]) == "Right":
                cost += curr[0][empty_tile]
                solution_moves.append((curr[0][empty_tile], "Left"))
            if (curr[-1]) == "Left":
                cost += curr[0][empty_tile]
                solution_moves.append((curr[0][empty_tile], "Right"))

            if curr > len(seq) - 1:
                end = False
        
        return solution_moves, solution_cost