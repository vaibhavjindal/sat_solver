QUESTION2

Program to generate SUDOKU+ puzzle

>HOW TO BUILD and RUN THE PROGRAM:
   1)Ensure that there are 6 files(including README.txt) in this folder and minisat and python3 are installed.
   2)Run the command "python3 generate_sud.py > gbg.txt" on the command line.
   3)A minimal SUDOKU+ puzzle will get printed in the file "output.txt".

>How it works:
  The program file "generate_sud.py" generates an unsolved minimal uniquely solvable puzzle in the file "output.txt". Garbage command line outputs are redirected to "gbg.txt".

>Brief logic behind the code:
  We take an empty puzzle and start filling numbers randomly in randomly selected cells. As soon as a number is filled in a cell, we put constraints such that the same number is not filled again in the same row, column, box or diagonal(in case of a diagonal cell) and that no other number can be filled in the same cell. We stop filling numbers as soon as we get a unique solution. From this puzzle, we remove every filled number, one at a time and check for multiple solutions. If the remaining puzzle has multiple solutions, then the number is replaced, else it remains removed. This procedure gives us a minimal puzzle.
  To check for multiple solutions, a solution is obtained and minisat is feeded with an extra condition which is the negation of the solution. If it is still SATISFIABLE, we have more than one solutions, else only a single solution.
