import protein_parser as pp

def main():
   folder = "PDBfiles/"
   print ("Executing this file as main show you the list of protein objects:")
   proteinas = pp.parse_proteins(folder)
   
   for element in proteinas:
      element.toString()
      

if __name__ == "__main__":
   main()