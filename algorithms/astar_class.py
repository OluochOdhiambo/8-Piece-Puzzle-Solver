import os
import argparse
import numpy as np
from datetime import datetime

def open_file(fname):
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

class AstarPuzzle:

    def __init__(self, start_node, target_node):
        self.start_node = start_node
        self.target_node = target_node

    def build_node(self, state, parent_node=None, action=None, node_depth=0, heuristic=0):
        return {
            'node state': state,
            'parent node': parent_node,
            'action': action,
            'node depth': node_depth,
            'heuristic': heuristic
        }
    
    def find_solution_path(self, node):
        solution_path = []
        cost = 0
        while node is not None:
            cost += node["heuristic"]
            solution_path.append((node['node state'], node['action']))
            node = node['parent node']
        solution_path.reverse()
        return solution_path, cost
    
    def swap_tiles(self, node, position1, position2):
        new_node = np.copy(node)
        temp = new_node[position1]
        new_node[position1] = new_node[position2]
        new_node[position2] = temp
        return new_node
    
    def explore_node(self, node):
        blank_tile_pos = np.where(node['node state'] == 0)[0][0]
        adjacent_nodes = []

        if blank_tile_pos not in [0, 1, 2]:
            adjacent_nodes.append(self.build_node(self.swap_tiles(node['node state'], blank_tile_pos, blank_tile_pos - 3), node, 'Up', node['node depth']+1, 0))
        if blank_tile_pos not in [0, 3, 6]:
            adjacent_nodes.append(self.build_node(self.swap_tiles(node['node state'], blank_tile_pos, blank_tile_pos - 1), node, 'Left', node['node depth']+1, 0))
        if blank_tile_pos not in [2, 5, 8]:
            adjacent_nodes.append(self.build_node(self.swap_tiles(node['node state'], blank_tile_pos, blank_tile_pos + 1), node, 'Right', node['node depth']+1, 0))
        if blank_tile_pos not in [6, 7, 8]:
            adjacent_nodes.append(self.build_node(self.swap_tiles(node['node state'], blank_tile_pos, blank_tile_pos + 3), node, 'Down', node['node depth']+1, 0))
           
        return adjacent_nodes
    
    def count_misplaced_tiles(self, node):
        misplaced_tiles = np.sum(node['node state'] != self.target_node)
        return misplaced_tiles
    
    def a_star_search(self, write_file):
        exp_n = 0
        gen_n = 0
        pop_n = 0
        max_fs = 0
        frontier = [(0, self.build_node(self.start_node))]

        while len(frontier) > 0:
            max_fs = max(max_fs, len(frontier))
            current_node = frontier.pop(0)[1]
            
            pop_n += 1
            

            if (current_node['node state'] == self.target_node).all():
                solution_path, cost = self.find_solution_path(current_node)
                return exp_n, gen_n, pop_n, max_fs, current_node['node depth'], current_node['heuristic'], solution_path

            if write_file != -1:

                with open(write_file, 'a') as file:
                    file.write(f"Generating successors to < state = {current_node}>" + '\n')
                    file.write(f"{len(self.explore_node(current_node))} successors generated" + '\n')
                    file.write(f"Closed: {current_node}" + '\n')
                    file.write(f"Fringe: {self.explore_node(current_node)}" + '\n')
            
            for child in self.explore_node(current_node):
                gen_n += 1
                child['heuristic'] = self.count_misplaced_tiles(child)
                frontier.append((child['heuristic'], child))
                frontier = sorted(frontier, key=lambda x: x[0])
            exp_n += 1

        return exp_n, gen_n, pop_n, max_fs, -1, -1, -1

    
    def track_solution_cost(self, seq):
        solution_moves = []
        solution_cost = 0

        end = True
        curr_idx = 0

        while end:
            curr_idx += 1
            prev_idx = curr_idx - 1

            prev = seq[prev_idx]
            curr = seq[curr_idx]

            empty_tile = np.where(prev[0] == 0)[0][0]
            if (curr[-1])  == "Down":
                solution_cost += curr[0][empty_tile]
                solution_moves.append((curr[0][empty_tile], "Up"))
            if (curr[-1]) == "Up":
                solution_cost += curr[0][empty_tile]
                solution_moves.append((curr[0][empty_tile], "Down"))
            if (curr[-1]) == "Right":
                solution_cost += curr[0][empty_tile]
                solution_moves.append((curr[0][empty_tile], "Left"))
            if (curr[-1]) == "Left":
                solution_cost += curr[0][empty_tile]
                solution_moves.append((curr[0][empty_tile], "Right"))

            if curr_idx > len(seq) - 2:
                end = False
        
        return solution_moves, solution_cost
        
    def print_styled(self, pop_n, exp_n, gen_n, max_fs, curr_d, cost, soln_moves):
        print(f'Nodes Popped: {pop_n}')
        print(f'Nodes Expanded: {exp_n}')
        print(f'Nodes Generated: {gen_n}')
        print(f'Max Fringe Size: {max_fs}')
        print(f'Solution found at depth {curr_d} with cost {cost}')
        print("Steps:")
        for move in soln_moves:
            print(f"Move {move[0]} {move[-1]}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="algorithmic solution of any 3*3 puzzle")
    parser.add_argument('--method', metavar='method', type=str, help='choose search algorithm', default="a*", choices=["bfs", "a*", "dfs", "dls", "ids", "greedy", "ucs"])
    parser.add_argument('--start', metavar='start.txt', type=str, help='contains start state of the puzzle')
    parser.add_argument('--goal', metavar='goal.txt', type=str, help='contains target state of the puzzle')
    parser.add_argument('--dump', help="write algorithm trace file", action='store_true')

    args = parser.parse_args()

    print(args)

    start = open_file("start")
    target = open_file("goal")
    method = args.method
    dump = args.dump

    print(args)

    if dump:
        trace_dump_path = f"trace_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        puzzle = AstarPuzzle(np.array(start), np.array(target))
        result = puzzle.a_star_search(trace_dump_path)
        exp_n, gen_n, pop_n, max_fs, soln_depth, soln_cost, soln_path = result
        if soln_path != -1:
            moves, cost= puzzle.track_solution_cost(soln_path)
            puzzle.print_styled(exp_n, gen_n, pop_n, max_fs, soln_depth, cost, moves)
        else: 
            print("Method could not find solution.")
    else:
        puzzle = AstarPuzzle(np.array(start), np.array(target))
        result = puzzle.a_star_search(-1)
        exp_n, gen_n, pop_n, max_fs, soln_depth, soln_cost, soln_path = result
        if soln_path != -1:
            moves, cost= puzzle.track_solution_cost(soln_path)
            puzzle.print_styled(exp_n, gen_n, pop_n, max_fs, soln_depth, cost, moves)
        else: 
            print("Method could not find solution.")