import os
import argparse
import subprocess
from datetime import datetime
from game_config.config_class import PuzzleConfig

parser = argparse.ArgumentParser(description="algorithmic solution of any 3*3 puzzle")
parser.add_argument('--method', metavar='method', type=str, help='choose search algorithm', default="a*", choices=["bfs", "a*", "dfs", "dls", "ids", "greedy", "ucs"])
parser.add_argument('--start', metavar='start.txt', type=str, help='contains start state of the puzzle')
parser.add_argument('--goal', metavar='goal.txt', type=str, help='contains target state of the puzzle')
parser.add_argument('--dump', help="write algorithm trace file", action='store_true')

args = parser.parse_args()

puzzle_config = PuzzleConfig()

start = puzzle_config.open_file("start")
target = puzzle_config.open_file("goal")
method = args.method
dump = args.dump


inversion_count = 0
for r in range(len(start)):
    for c in range(r + 1, len(start)):
        if start[r] != 0 and start[c] != 0 and start[r] > start[c]:
            inversion_count += 1

if inversion_count % 2 != 0:
    print("Puzzle not solvable")
else:
    write_path = -1
    if dump:
        write_path = f"trace_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        with open(write_path, 'w') as trace_file:
                trace_file.write(f"Command-Line Arguments : ['start.txt', 'goal.txt', '{str(method)}', '{str(dump)}']" + '\n')
                trace_file.write(f"Method selected: {str(method)}" + '\n')

    if method == "a*":
        method_path = os.path.join("algorithms", "astar_class.py")
        subprocess.run(['python', method_path, "--start", "start.txt", "--goal", "goal.txt"] + (["--dump"] if dump else []))

    if method == "greedy":
        method_path = os.path.join("algorithms", "greedy_class.py")
        subprocess.run(['python', method_path, "--start", "start.txt", "--goal", "goal.txt"] + (["--dump"] if dump else []))

    if method == "bfs":
        method_path = os.path.join("algorithms", "bfs_class.py")
        subprocess.run(['python', method_path, "--start", "start.txt", "--goal", "goal.txt"] + (["--dump"] if dump else []))

    if method == "dfs":
        method_path = os.path.join("algorithms", "dfs_class.py")
        subprocess.run(['python', method_path, "--start", "start.txt", "--goal", "goal.txt"] + (["--dump"] if dump else []))

    if method == "dls":
        method_path = os.path.join("algorithms", "dls_class.py")
        subprocess.run(['python', method_path, "--start", "start.txt", "--goal", "goal.txt"] + (["--dump"] if dump else []))

    if method == "ids":
        method_path = os.path.join("algorithms", "ids_class.py")
        subprocess.run(['python', method_path, "--start", "start.txt", "--goal", "goal.txt"] + (["--dump"] if dump else []))

    if method == "ucs":
        method_path = os.path.join("algorithms", "ucs_class.py")
        subprocess.run(['python', method_path, "--start", "start.txt", "--goal", "goal.txt"] + (["--dump"] if dump else []))