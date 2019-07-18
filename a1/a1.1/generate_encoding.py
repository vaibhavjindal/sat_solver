#Program to generate cnf encoding 
import sys

# We are using 729 premises in this program.
# If (i,j)th cell contains the integer k then it corresponds to premise number (k-1)*81+(i-1)*9+j (where i,j starts from 1)
# For example, 
# Premise "9" is true 9th if cell of the 1st row is 1
# Premise "82" is true if 1st cell of the 1st row is 2
# Premise "729" is true if 9th cell of the 9th row is 9

#input.txt contains the given input
input_file=open('input.txt','r')
# open the input file       
a = input_file.read().splitlines()     
# to store the corresponding premises for the fixed numbers in the array "ones"
ones=[] 
for i in range(9):
	for j in range(9):
		if(a[i][j] is '.'):
			pass
		else:
			ones.append(9*i+j+1+81*(int(a[i][j])-1))    

input_file.close()

#to write encoding in "encoding.txt"
orig_stdout = sys.stdout
f = open('encoding.txt', 'w')
sys.stdout = f

# function to write encoding to ensure that no two premises in array "a" become true simultaneously  
def f(a):
    for k in range(9):
        for i in range(k+1,9):
            print(str(-a[k])+" "+str(-a[i])+" "+"0")

# first line of encoding with 12654+len(ones) clauses and 729 premises           
print("p"+" "+"cnf"+" "+"729"+" "+str(12654+len(ones)))
#temporary array to store premises such that at least one of them is true
a=[]

#each cell should have exactly one value
for x in range(81):
    for k in range(9):
        #a cell should have atleast one value
        print(str(x+k*81+1)+" ",end="")
        a.append(x+k*81+1)
    print("0")
    #a cell should not have two values
    f(a)
    del a[:]

#each row should have a particular value exactly one time
for x in range(9):
    for k in range(9):
        for p in range(9):
            print(str(x*81+k*9+1+p)+" ",end="")
            a.append(x*81+k*9+1+p)
        print("0")
        f(a)
        del a[:]

#each column should have a particular value exactly one time
for x in range(9):
    for k in range(9):
        for p in range(9):
            print(str(x*81+k+1+p*9)+" ",end="")
            a.append(x*81+k+1+p*9)
        print("0")
        f(a)
        del a[:]

#each box should have a particular value exactly one time
for x in range(9):
    for p in range(3):
        for k in range(3):
            for l in range(3):
                for m in range(3):
                    print(str(x*81+p*27+3*k+9*l+m+1)+" ",end="")
                    a.append(x*81+p*27+3*k+9*l+m+1)
            print("0")
            f(a)
            del a[:]

#diagonal 1 should have each value exactly one time
for x in range(9):
    for k in range(9):
	    print(str(x*81+10*k+1)+" ",end="")
	    a.append(x*81+10*k+1)
    print("0")
    f(a)
    del a[:]      

#diagonal 2 should have each value exactly one time   
for x in range(9):
    for k in range(9):
	    print(str(x*81+8*k+9)+" ",end="")
	    a.append(x*81+8*k+9)
    print("0")
    f(a)
    del a[:]  

#premises corresponding to input puzzle must be true
for i in ones:
	print(str(i)+" "+"0")


#to print to a file
sys.stdout = orig_stdout
