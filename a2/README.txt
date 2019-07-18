ASSIGNMENT 2

Please ensure that there are five(excluding assignment2.pdf) files in the folder.

HOW TO RUN:
->Paste the cnf code in the file "input.txt".
->Compile the cpp file "solver" using g++ compiler using the command "g++ solver.cpp".
->Invoke the executable file "a.out" to run the program by typing "./a.out".
->The solution can be found in the file "output.txt" after the code has been executed.

HEURISTICS USED IN THE PROGRAM:
-> The smallest clause is first selected.
-> Then we find within that selected clause the literal which appears maximum number of times in the complete formula.
-> Then we break the clause at that literal. For this, we first assume that the literal is true and then trim the encoding accordingly. If we obtain a 
   SATISFIABLE interpretation, we are done. Otherwise we assume the literal to be false and repeat the process again.


For the following minimal sudoku generated from our program for assignment 1,

.38.2...4
...3..7..
.9.......
2.....4..
8..6....1
5....2.39
.........
.....1...
....8....

this program made 38301 decompositions(recursive calls) on the sudoku solver encoding generated as a part of assignment 1.
