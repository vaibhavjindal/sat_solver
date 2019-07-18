import random #for random number generator
import os #for terminal commands

#returns the value which a premise "n" gives to a cell
def val(n):
	return int((n-1)/81)+1

#returns the row,column,cell number(1-81), box number(1-9) for a premise "n"
def info(n):
	cell=n-(val(n)-1)*81
	row=int((cell-1)/9)+1
	col=cell%9
	if(col==0):
		col=9
	box=(int((row-1)/3))*3+(int((col-1)/3)+1)
	return row,col,cell,box

#for a premise "n", it removes out other premises from the allowed array("a") that are not allowed
def trim_a(a,n):
	value=val(n)
	row,col,cell,box=info(n)
	
	# removes the premises for other values of the same cell since a value has been alloted to the cell
	for i in range(9):
		if((cell+i*81) in a):
			a.remove(cell+i*81)
	#no other cell in the row should have the same value
	for i in range(9):
		if ((row-1)*9+i+1+81*(value-1)) in a:
			a.remove((row-1)*9+i+1+81*(value-1))
	#no other cell in the column should have the same value
	for i in range(9):
		if (col+i*9+81*(value-1)) in a:
			a.remove(col+i*9+81*(value-1))
	#no other cell in the box should have the same value
	for r in range(int((box-1)/3)*3+1,int((box-1)/3)*3+4):
		temp=box%3
		if(temp==0):
			temp=3
		for c in range((temp-1)*3+1,(temp-1)*3+4):
			if (r-1)*9+c+81*(value-1) in a:
				a.remove((r-1)*9+c+81*(value-1))
	#if the cell is in the first diagonal, no other element in the diagonal should have the same value
	if(row==col):
		for i in range(9):
			r=i+1
			c=i+1
			if (r-1)*9+c+(value-1)*81 in a:
				a.remove((r-1)*9+c+(value-1)*81)
	#if the cell is in the second diagonal, no other element in the diagonal should have the same value
	if(row+col==10):
		for i in range(9):
			r=i+1
			c=10-r
			if (r-1)*9+c+(value-1)*81 in a:
				a.remove((r-1)*9+c+(value-1)*81)
				print((r-1)*9+c+(value-1)*81)

#same function as in part 1 of the question, only "en_file" parameter added to write to "en_file" object
def f(a,en_file):
	for k in range(9):
		for i in range(k+1,9):
			en_file.write(str(-a[k])+" "+str(-a[i])+" "+"0\n")

#same encoding as in part 1 of the question
#only "string" parameter added to write negation of a solution while checking multiple solutions
#writes the encoding in "encoding.txt" file
def gen_encoding(arr,string):
	#if string parameter is empty, then same encoding as in part 1
	if(string==""):
		en_file=open("encoding.txt","w")	
		en_file.write("p"+" "+"cnf"+" "+"729"+" "+str(12654+len(arr))+"\n")
		a=[]
		for i in arr:
			en_file.write(str(i)+" "+"0\n")

		for x in range(81):
			string=""
			for k in range(9):
				string=string+(str(x+k*81+1)+" ")
				a.append(x+k*81+1)
			string=string+"0\n"
			en_file.write(string)
			f(a,en_file)
			del a[:]

		for x in range(9):
			for k in range(9):
				string=""
				for p in range(9):
					string=string+(str(x*81+k*9+1+p)+" ")
					a.append(x*81+k*9+1+p)
				string=string+"0\n"
				en_file.write(string)
				f(a,en_file)
				del a[:]
		for x in range(9):
			for k in range(9):
				string=""
				for p in range(9):
					string=string+(str(x*81+k+1+p*9)+" ")
					a.append(x*81+k+1+p*9)
				string=string+"0\n"
				en_file.write(string)
				f(a,en_file)
				del a[:]
		for x in range(9):
			for p in range(3):
				for k in range(3):
					string=""
					for l in range(3):
						for m in range(3):
							string=string+(str(x*81+p*27+3*k+9*l+m+1)+" ")
							a.append(x*81+p*27+3*k+9*l+m+1)
					string=string+"0\n"
					en_file.write(string)
					f(a,en_file)
					del a[:]
		for x in range(9):
			string=""
			for k in range(9):
				string=string+(str(x*81+10*k+1)+" ")
				a.append(x*81+10*k+1)
			string=string+"0\n"
			en_file.write(string)
			f(a,en_file)
			del a[:]	 
		for x in range(9):
			string=""
			for k in range(9):
				string=string+(str(x*81+8*k+9)+" ")
				a.append(x*81+8*k+9)
			string=string+"0\n"
			en_file.write(string)
			f(a,en_file)
			del a[:]  
		en_file.close()

	#if string parameter contains a negation of a solution, then string also added to the solution
	else:
		en_file=open("encoding.txt","w")	
		en_file.write("p"+" "+"cnf"+" "+"729"+" "+str(12654+len(arr)+1)+"\n")#"+1" to account for string
		en_file.write(string+"0\n")
		a=[]
		for i in arr:
			en_file.write(str(i)+" "+"0\n")

		for x in range(81):
			string=""
			for k in range(9):
				string=string+(str(x+k*81+1)+" ")
				a.append(x+k*81+1)
			string=string+"0\n"
			en_file.write(string)
			f(a,en_file)
			del a[:]

		for x in range(9):
			for k in range(9):
				string=""
				for p in range(9):
					string=string+(str(x*81+k*9+1+p)+" ")
					a.append(x*81+k*9+1+p)
				string=string+"0\n"
				en_file.write(string)
				f(a,en_file)
				del a[:]
		for x in range(9):
			for k in range(9):
				string=""
				for p in range(9):
					string=string+(str(x*81+k+1+p*9)+" ")
					a.append(x*81+k+1+p*9)
				string=string+"0\n"
				en_file.write(string)
				f(a,en_file)
				del a[:]
		for x in range(9):
			for p in range(3):
				for k in range(3):
					string=""
					for l in range(3):
						for m in range(3):
							string=string+(str(x*81+p*27+3*k+9*l+m+1)+" ")
							a.append(x*81+p*27+3*k+9*l+m+1)
					string=string+"0\n"
					en_file.write(string)
					f(a,en_file)
					del a[:]
		for x in range(9):
			string=""
			for k in range(9):
				string=string+(str(x*81+10*k+1)+" ")
				a.append(x*81+10*k+1)
			string=string+"0\n"
			en_file.write(string)
			f(a,en_file)
			del a[:]	 
		for x in range(9):
			string=""
			for k in range(9):
				string=string+(str(x*81+8*k+9)+" ")
				a.append(x*81+8*k+9)
			string=string+"0\n"
			en_file.write(string)
			f(a,en_file)
			del a[:]  
		en_file.close()


# for an array of premises, it checks whether the solution exists, is unique or has multiple solutions
def num_sols(arr):
	
	#generate encoding for the array
	gen_encoding(arr,"")
	# invokes minisat to output result for the generated encoding in "enc_out.txt"
	os.system("minisat encoding.txt enc_out.txt")
	
	#read the minisat solution from "enc_out.txt"
	f=open('enc_out.txt','r')
	a = f.read().splitlines()
	f.close()

	#no solution for the array
	if(a[0]=="UNSAT"):
		return 0
	# if solution exists for the array, append the negation of solution in encoding and check for another solution
	else: 
		#read the minisat result and generate a new encoding with negation of result stored in variable string
		a.pop(0)
		b=a[0].split(" ")
		b.pop(-1)
		arr2=[i for i in arr]
		string=""
		for j in b:
			if(int(j)>0):
				if int(j) not in arr2:
					string=string+str(-int(j))+" "
		gen_encoding(arr2,string)

		#read the minisat output again and store it in data variable
		os.system("minisat encoding.txt enc_out.txt")
		f=open('enc_out.txt','r')
		data = f.read().splitlines()
		f.close()
		
		if(data[0]=="UNSAT"):
			# array has exactly one solution
			return 1
		else:
			# array has multiple solutions
			return 2

#for a given array of premises with a unique solution, removes some elements so as to make it minimal
def make_minimal(arr):
	length=len(arr)
	for i in range(length):
		#remove the first element of the array
		num=arr.pop(0)
		#if multiple solutions, then append the element agin to the list
		if(num_sols(arr)==2):
			arr.append(num)
		#if single solution, then don't add the element again
		elif(num_sols(arr)==1):
			pass

#writes the final solution in "puzzle.txt"
def write_puzzle(arr):
	f=open('puzzle.txt','w')
	arr2=[["." for x in range(9)] for y in range(9)]
	for i in arr:
		value=val(i)
		row,col,cell,box=info(i)
		arr2[row-1][col-1]=str(value)
	for i in range(9):
		for j in range(9):
			f.write(arr2[i][j])
		f.write("\n")
	f.close()

#main driver function
def main():
	#array for allowed premises(1-729)
	allowed=[i+1 for i in range(729)]
	#array for selected premises
	filled=[]

	while(True):
		#append a random premise from allowed premises to filled
		index=random.randint(0,len(allowed)-1)
		num=allowed[index]
		filled.append(num)
		#nos is number of solutions for the filled array
		nos=num_sols(filled)
		#if more than 1 solutions
		if(nos==2):
			#remove unallowed premises from allowed array corresponding to num
			trim_a(allowed,num)
		#if one solution only
		elif(nos==1):
			#got a unique solution, break from while loop
			break
		#if no solution, remove the last premise from filled and allowed
		elif(nos==0):
			filled.pop(-1)
			allowed.remove(num)
	#make the solution minimal
	make_minimal(filled)
	#write the puzzle in "puzzle.txt"
	write_puzzle(filled)

#invoking the main function
main()

