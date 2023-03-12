# 8-Piece Puzzle Solver
![8puzzlegame](https://user-images.githubusercontent.com/63576010/224524425-0b2599d0-cc81-4811-94e4-3db08ab0bda3.png)

## About
The 8-puzzle is a sliding puzzle that consists of a 3x3 grid with eight numbered tiles and one blank space. The eight numbered tiles are initially placed in a random order within the grid, and the objective of the puzzle is to rearrange the tiles by sliding them into the blank space until they are in ascending order, with the blank space in the bottom right corner. The puzzle is a classic problem in artificial intelligence and has been used to demonstrate various search algorithms and is also a popular puzzle game that has been enjoyed by many people for generations.

## Technical Requirements
The project is built as a command-line application where the script takes 4 optional arguments:

- Method - which specifies the search algorithm to use.
- Start - which specifies the initial state of the puzzle
- Goal -  which specifies the goal state of the puzzle
- Dump - which sets the option to write a trace file to examine the performance of each algorithm
   
![solution guide](https://user-images.githubusercontent.com/63576010/224524444-9f3f1778-b321-443c-b3c3-747219a8ecce.png)

## Installation and Setup
To run the 8-puzzle solver, follow these steps:

1. Clone the repository
2. Install Python 3.6 or higher
3. Run the solver using python main.py --start [start.txt] --goal [goal.txt]

The default algorithm is set to breadth-first search. To test other algorithms, use the --method flag:

#### python main.py --start [start.txt] --goal [goal.txt] --method a*

To examine and/or compare performance of the algorithms, use the --dump flag to write performance metrics to a .txt file:

#### python main.py --start [start.txt] --goal [goal.txt] --method a* --dump

## Usage 
The 8-puzzle solver allows you to find the optimal solution to any 8-puzzle by providing the initial and goal states. The following search algorithms are available:

- Breadth first search
- Depth first search
- Depth limited search
- A* search
- Greedy search
- Uniform cost search
- Iterative deepening search

## Contributing
Contributions to this project are welcome. If you would like to contribute, please follow these steps:

1. Fork the repository
2. Make your changes
3. Create a pull request

## Credits
I would like to credit the following sources:

- Artificial Intelligence: A Modern Approach, by Stuart Russell and Peter Norvig
- Python documentation

## License
This project is licensed under the MIT License.

## Contact
If you have any questions or concerns about the 8-puzzle solver, please contact me at [oluochodhiambo11@gmail.com].
