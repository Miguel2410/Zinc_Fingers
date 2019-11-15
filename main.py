import protein_parser as pp

def main():
   folder = "PDBfiles/"
   print ("Executing this file as main show:")
   proteinas = pp.parse_proteins(folder)

   for element in proteinas:
      #element.toString()
      for element2 in proteinas:
         print (element.name, element2.name, element.distance(element2))


if __name__ == "__main__":
   main()
