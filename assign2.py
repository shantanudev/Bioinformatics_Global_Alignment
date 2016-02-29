import numpy as np
import sys


def lookup():
    sub_mat = open("subs.txt", "r")
    sub = sub_mat.read()
    sub = sub.split()
    
    names = ["A", "C", "G", "T"]
    
    sub_lookup = {}
    counter = 5
    for counter_x, x in enumerate(names):
   	for counter_y, y in enumerate(names):
  		sub_lookup[x + y] = int(sub[counter])
  		counter = counter + 1
  		if (counter - 4) % 5 == 0:
 			counter = counter + 1
    return sub_lookup

def backtrace(x, y):

    global seq1_x, seq2_x 
 
    
    if(x <= 0 and y <= 0):
        print 'sequence1 = ' , seq1_x[::-1]
        print 'sequence2 = ' , seq2_x[::-1]
        return        
    elif x >= 0 and ((matrix[y][x] - matrix[y-1][x]) == gap_penalty):
        #Check Up to get the gap
        
        seq1_x+="-"       
        seq2_x+=seq2[y-1]     
        backtrace(x, y - 1)
    elif y >= 0 and ((matrix[y][x] - matrix[y][x-1]) == gap_penalty):
        #Checks the left to get gap
                
        seq1_x+=(seq1[x-1])
        seq2_x+="-"      
        backtrace(x - 1, y)

    else:
        seq1_x+=seq1[x-1]
        seq2_x+=seq2[y-1]
        backtrace(x - 1, y - 1)

#The arguments that are passed into Pytho file which are parsed
sequence1 = open(sys.argv[1],"r")
sequence2 = open(sys.argv[2],"r")
sub = open(sys.argv[3],"r")
gap_penalty = int(sys.argv[4])

seq1list = sequence1.read().split()
seq1 = seq1list[-1].strip()
n = len(seq1) + 1

seq2list = sequence2.read().split()
seq2 = seq2list[-1].strip()
m = len(seq2) + 1

matrix = [[0 for x in range(n)] for y in range(m)]
gap_penalty_x = gap_penalty
for x in xrange(1,n):  
   matrix[0][x] += gap_penalty_x 
   gap_penalty_x += gap_penalty  
gap_penalty_y = gap_penalty
for y in xrange(1,m):
    matrix[y][0] += gap_penalty_y
    gap_penalty_y += gap_penalty

sub_value = lookup()
for x in xrange(1, n):
    for y in xrange(1, m):
        a = str(seq1[x-1])
        b = str(seq2[y-1])
        matrix[y][x] = max((matrix[y][x-1] + gap_penalty), (matrix[y-1][x] + gap_penalty), (matrix[y-1][x-1] + sub_value[a+b]))
        
x = matrix[m-1][n-1]

print "The optimal alignment between given sequences has score " + str(x)+"."
seq1_x = ""
seq2_x = ""
backtrace(n - 1, m - 1)


        

