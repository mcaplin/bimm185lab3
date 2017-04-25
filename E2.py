import gzip
from Bio import SeqIO

inp = gzip.open('GCF_000005845.2_ASM584v2_protein.faa.gz', 'rb') # unzip file
out = open('E2_out.txt', 'w') # create output file

for record in SeqIO.parse(inp, "fasta"): # parse each record
    out.write(str(record.id) + '\t' + str(record.seq) + '\n') # put in the record id and the sequence
    
inp.close()
out.close()