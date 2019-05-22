__author__ = "Yao-Yin"

from Bio import Entrez
from Bio import SeqIO

f_in = open(str(input("""Please input your reference txt\nEg. D:\\test.txt""")),'r')
ref_list = f_in.readlines()
id_array = []
for ref in ref_list[1:]:
    Ref = ref.split(',')
    new = Ref[0].strip()
    id_array.append(new)

Entrez.email = input("Please input your email address")

f_out_name = input("Please input the name of your output file\nEg: D:\\test.fasta")
f_out = open(f_out_name, "w+")
for record_id in id_array:
    try:
        resulthandle = Entrez.efetch(db="nucleotide", rettype="gb", id=record_id, retmode="text")
        seqRecord = SeqIO.read(resulthandle, format="gb")
        resulthandle.close()
        f_out.write((seqRecord.format("fasta")))
    except:
        continue
f_out.close()
f_in.close()