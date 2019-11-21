import protein_parser as pparser
from KD_tree import construct_kd_tree
from Protein import Protein
import argparse

import argparse

parser = argparse.ArgumentParser(description='KDtree building app.')

parser.add_argument('-print_tree', action="store_true", default=False)
parser.add_argument('-PDBfolder', action="store", dest="folder", help="This is the folder with the PDB files")
parser.add_argument('-check_closest', action="store", dest="closest", help="Tupple of 10 dimensions with the point you want to check the closes protein")
parser.add_argument('-test', action ="store_true", default=False, help="This argument prints the tree and the nearest point of a testing value")


args = parser.parse_args()

if args.test:
	closest = (0 , 0 , 0 , 0 , 0 , 0 , 2 , 0.16981132075471697 , 2 , 0.02358490566037736)


dimensions = 10

def main():
	Protein_dict = pparser.parse_proteins(args.folder)
	kdtree = construct_kd_tree(Protein_dict, 10)

	if args.print_tree or args.test:
		print (kdtree.toJson(),"\n")

	if 'closest' in vars() or args.test:
		kdtree.nearest_neighbor(closest)

	
if __name__ == "__main__":
	main()
