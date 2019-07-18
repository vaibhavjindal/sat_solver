QUESTION1

> Program to solve SUDOKU+

>HOW TO BUILD and RUN THE PROGRAM:
	1)Ensure that there are 9 files(including README.txt) in this folder and minisat and python3 are installed.
	2)Give input in the file "input.txt" as mentioned in question(nine lines with each line containing nine characters(without space) with empty cells reprsented by ".").
   	3)Run "python3 run.py > gbg.txt" on command line.
    4)The solved SUDOKU+ will get printed in the file "output.txt". 

>How it works:
  The program "run.py" first calls "generate_encoding.py" which writes the cnf encoding in "encoding.txt". Then "run.py" invokes minisat to take input from "encoding.txt" and write its output in "minisat_output.txt". Finally "run.py" calls "decode.py" which converts the output from minisat to a readable sudoku format and writes it in the file "output.txt". Garbage command line outputs are redirected to "gbg.txt".


> Brief logic behind the solution:
  A total of 729 premises are formed considering the fact that each of 81 cells can have any number from 1 to 9. Encoding is then generated such that each row, column, diagonal and box contains every number from 1 to 9 exactly once and each cell contains exactly one element. Input puzzle conditions are also encoded in the encoding. SAT solver is then invoked to check for SATIFIABILITY and the solution is printed if the encoding is satisfiable.
