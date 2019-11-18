import protein_parser as pparser
from kdtree import parse_protein_list, kd_tree
import pprint


pp = pprint.PrettyPrinter(indent=4)

for element in pparser.parse_proteins("PDBfiles/"):
	for element2 in pparser.parse_proteins("PDBfiles/"):
		print(element.name, element2.name, element.distance(element2))


dimensions = 10


def main():
   folder = "PDBfiles/"
   print ("Executing this file as main show:")
   proteinas = pparser.parse_proteins(folder)
   coords = parse_protein_list(proteinas)
   pp.pprint(kd_tree(coords, dimensions, depth=0))


if __name__ == "__main__":
   main()
   parse_protein_list(pparser.parse_proteins("PDBfiles/"))