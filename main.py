import protein_parser as pp
import KDTree as kdt

def main():
   folder = "PDBfiles/"
   print ("Executing this file as main show:")
   proteinas = pp.parse_proteins(folder)

   kdtree = kdt.KDNode(dimensions=9)
   
   print(proteinas[0].name)
   print(proteinas[4].name)
   print(proteinas[3].name)


   protein1 = (proteinas[0].C2H2, proteinas[0].C2WH2, proteinas[0].GATA3, proteinas[0].CCHC, proteinas[0].ZN2C6, proteinas[0].hys_cys, proteinas[0].prot_len, proteinas[0].num_chain, proteinas[0].pos)
   protein2 = (proteinas[4].C2H2, proteinas[4].C2WH2, proteinas[4].GATA3, proteinas[4].CCHC, proteinas[4].ZN2C6, proteinas[4].hys_cys, proteinas[4].prot_len, proteinas[4].num_chain, proteinas[4].pos)
   protein3 = (proteinas[3].C2H2, proteinas[3].C2WH2, proteinas[3].GATA3, proteinas[3].CCHC, proteinas[3].ZN2C6, proteinas[3].hys_cys, proteinas[3].prot_len, proteinas[3].num_chain, proteinas[3].pos)

   #kdtree.add(protein1)
   kdtree.add(protein3)
   print(kdtree.dist(protein2))
   
  

if __name__ == "__main__":
   main()
