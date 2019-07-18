#to give terminal commands
import os

#running generate_encoding.py to generate the encoding
os.system("python3 generate_encoding.py")
#invoking minisat on the encoding and storing the output in "minisat_output.txt"
os.system("minisat encoding.txt minisat_output.txt")
#decoding the minisat output
os.system("python3 decode.py")
