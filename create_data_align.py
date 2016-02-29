import random
import sys
import subprocess

global nucleotide
nucleotide=["A", "C", "G", "T"]

def mutate(seq):
	seq=list(seq)
	seq_len=len(seq)
	num_mut=int(seq_len/10)
	
	for i in range(0,num_mut):
		coin_flip=random.randrange(0,2)
		ind=random.randrange(0,100)
		nucleotide_rand=random.randrange(0,4)
		if coin_flip==1:
			seq[ind]=nucleotide[nucleotide_rand]
			coin_flip=random.randrange(0,2)
			if coin_flip==1:
				seq[ind]=""

	seq=reduce(lambda a,b:a+b,seq)
	return seq
		


bp_length=int(sys.argv[1])
seq1=""

for i in range(0,bp_length):
	nucleotide_rand=random.uniform(0,10)
	if nucleotide_rand<=2.5 and nucleotide>=0:
		nucleotide_rand=0
	elif nucleotide_rand<=5 and nucleotide>2.5:
		nucleotide_rand=1
	elif nucleotide_rand<=7.5 and nucleotide>5:
		nucleotide_rand=2
	else:
		nucleotide_rand=3
	seq1=nucleotide[nucleotide_rand]+""+seq1

#creates files for Seq1 mutation to be read later
seq2=">seq2\n"+mutate(seq1)
with open("s2.txt", 'w') as f:
	f.write(seq2)
seq3=">seq3\n"+mutate(seq1)
with open("s3.txt", 'w') as f:
	f.write(seq3)

line=subprocess.check_output("python assign2.py s2.txt s3.txt subs.txt -500", shell=True)
with open(sys.argv[2], 'w') as f:
	f.write(str(line))