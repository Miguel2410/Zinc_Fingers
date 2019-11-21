import os, sys
from Bio import SeqIO
import Bio.motifs as motifs
from Protein import Protein
import re

def parse_proteins(directory):

    proteins = list()

    #First we parse the structure.
    for file in os.listdir(directory):

        ZN_num = 0
        length = 0
        Hys_Cys = 0
        ARG_LYS_HIS = 0
        C2H2_occur = 0
        C2WH2_occur = 0
        GATA3_occur = 0
        CCHC_occur = 0
        ZN2C6_occur = 0
        length_factor = 0

        if file.endswith(".pdb") or file.endswith(".ent") or file.endswith(".cif"):
            # Check the Zinc ions
            with open(os.path.join(directory,file),"r") as pdb:
                for line in pdb:
                    if line.startswith("HETNAM"):
                        if line.split(" ")[1] == "ZN":
                            ZN_num += 1

            # Biopython parser.
            protein = SeqIO.to_dict(SeqIO.parse((os.path.join(directory,file)), "pdb-seqres"))
            
            #Number of chains
            chain_num = len(protein)  #Number of chains
            for key in (protein.keys()):

                #C2H2 Motif
                C2H2 = re.findall("[C].{2,4}[C].{9,13}[H].{3,5}[H]", str(protein[key].seq))
                C2H2_occur = C2H2_occur + len(C2H2)

                #C2WH2 Motif
                C2WH2 = re.findall("[C].[W].{1,4}[C].{2,13}[H].{3,5}[H]", str(protein[key].seq))
                C2WH2_occur = C2WH2_occur + len(C2WH2)

                #GATA3 Motif
                GATA3 = re.findall("[Y].[K].[H].{1,3}[R][P]", str(protein[key].seq))
                GATA3_occur = GATA3_occur + len(GATA3)

                #CCHC Motif
                CCHC = re.findall("[C]..[C].{3,4}[H].{5,7}[C]", str(protein[key].seq))
                CCHC_occur = CCHC_occur + len(CCHC)

                #ZN2C6 Motif
                ZN2C6 = re.findall("[C]..[C]...[KR].[KR][C].{5,7}[C]..[C].{5,7}[C]", str(protein[key].seq))
                ZN2C6_occur = ZN2C6_occur + len(ZN2C6)

                # Length of total protein
                length = length + (len(protein[key].seq))

                #Number of Hystidines + Cysteine
                Hys = (str(protein[key].seq).count("H"))
                Cys = (str(protein[key].seq).count("C"))
                Hys_Cys = Hys_Cys + Hys + Cys  

                #Number of positive residues in the protein
                ARG =  (str(protein[key].seq).count("R"))
                LYS =  (str(protein[key].seq).count("K"))
                ARG_LYS_HIS = ARG_LYS_HIS + Hys + ARG + LYS

            if 200 > length > 0:
                length_factor = 0
            elif 400  >= length >= 200:
                length_factor = 1
            elif 600 >= length > 400:
                length_factor = 2
            else:
                length_factor = 3
            
            prot = Protein(
                    name = file[:-4],
                    C2H2 = C2H2_occur,
                    C2WH2 = C2WH2_occur,
                    GATA3 = GATA3_occur, 
                    CCHC = CCHC_occur, 
                    ZN2C6 = ZN2C6_occur, 
                    zinc=ZN_num, 
                    prot_len=length_factor, 
                    pos=ARG_LYS_HIS/length, 
                    num_chain=chain_num, 
                    hys_cys=Hys_Cys/length)
            
            proteins.append(prot)

    return proteins

if __name__ == "__main__":
    print ("Executing this file as main show you the list of protein objects:")
    #print(parse_proteins(folder))