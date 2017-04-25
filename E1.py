import gzip
from Bio import SeqIO

inp = gzip.open('GCF_000005845.2_ASM584v2_genomic.gbff.gz', 'rb') # unzip file
extract = ['protein_id', 'gene', 'locus_tag', 'gene_synonym', 'product', 'EC_number', 'db_xref'] # list of some of the things we will extract

s = {} # dictionary to organize the data we are extracting
i = 0 # iterator key to keep track of dictionary items
taxon = False
for record in SeqIO.parse(inp, "genbank"): # parse each record of the file
    if record.features: 
        for feature in record.features: # features, most of them are "CDS" and "gene"
            if feature.type == "source": # to get the taxon
                s[i] = []
                if 'db_xref' in feature.qualifiers:
                    s[i].append(str(feature.qualifiers['db_xref']))
                    taxon = True # so we don't reset the key when we get to the next feature
            if feature.type == "CDS": # most of the data we extract comes from CDS
                if taxon == False: # If it doesn't have a tax ID
                    s[i] = []
                    s[i].append("-------")
                s[i].append(str(feature.location.start) + ', ' + str(feature.location.end)) # Extract coordinates
                s[i].append(feature.location.strand) # Extract strand
                for e in extract:
                    if e in feature.qualifiers:
                        s[i].append(str(feature.qualifiers[e])) # Extract all the other qualifiers
                    else:
                        s[i].append("-------") # If the CDS doesn't have a qualifier put a bunch of dashes instead
                taxon = False
                i += 1

out = open('E1_Out.txt', 'w')

for j in s: # Write to output file
    out.write(str(s[j][3]) + '\t' + str(s[j][1]) +'\t' + str(s[j][2]) + '\t' + str(s[j][4]) + '\t' + str(s[j][5]) + '\t' + str(s[j][6]) + '\t' + str(s[j][7]) + '\t' + str(s[j][0]) + '\t' + str(s[j][8]) + '\t' + str(s[j][9]) + '\n')

inp.close()
out.close()
