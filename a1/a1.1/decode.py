#Program to convert output from minisat to readable sudoku format and write it to "output.txt"

#to output the result to "output.txt"
import sys
orig_stdout = sys.stdout
f = open('output.txt', 'w')  
sys.stdout = f

 #reading and storing minisat output in a
input_file=open('minisat_output.txt','r')      
a = input_file.read().splitlines()

#if unsolvable
if(a[0]=="UNSAT"):                               
	print("UNSAT")
	pass
#if solution exoits
else:
	# converts the output from minisat to final sudoku format and stores in 2D list "c"
	a.pop(0)
	b = a[0].split(" ")
	b.pop(-1)
	c=[['0' for j in range(9)] for i in range(9)]  
	for j in b:
		k=int(j)
		if(k>0):
			l=int(int((k-1)/81)+1)
			m=k-(l-1)*81
			row=int((m-1)/9)
			col=(m-1)%9
			c[row][col]=l

	#to print the output
	for i in range(9):
		for j in range(9):
			print(c[i][j],end="")
		print("")
sys.stdout = orig_stdout
