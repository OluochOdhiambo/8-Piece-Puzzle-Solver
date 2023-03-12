# 8-Piece Puzzle Solver
![8puzzlegame](https://user-images.githubusercontent.com/63576010/219436487-3364acfa-33d2-492f-ac28-40ac823f97c2.png)

## About
The 8-piece-puzzle is a sliding puzzle that consists of a 3x3 grid with eight numbered tiles and one blank space. The eight numbered tiles are initially placed in a random order within the grid, and the objective of the puzzle is to rearrange the tiles by sliding them into the blank space until they are in ascending order, with the blank space in the bottom right corner. The puzzle is a classic problem in artificial intelligence and has been used to demonstrate various algorithms such as breadth-first search, depth-first search, and A\* search. It is also a popular puzzle game that has been enjoyed by many people for generations.

This project implements the breadth-first search, depth-first search, and A\* search algorithms to solve any 8 piece puzzle. The project is built as a command line application where the script takes 4 optional arguments namely: search algorithm, initial puzzle state, goal puzzle state, and dump flags.

## Usage

1. Clone the file to a local repository.
2. Open the command line and run:
   python solver.py --initial_state [some state] --goal_state [some state]
3. The default algorithm is set to breadth-first search. To test other algorithms, use the --heuristic_search flag
   python solver.py --initial_state [some state] --goal_state [some state] --heuristic_search a\*
4. To examine and/or compare performance of the algorithms, use the --dump flag to write performance metrics to a .txt file
   python solver.py --initial_state [some state] --goal_state [some state] --heuristic_search a\* --dump True
   
![run](https://user-images.githubusercontent.com/63576010/219437899-42e9f799-62d3-4190-837f-73a69741207c.png)
