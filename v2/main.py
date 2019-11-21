import protein_parser as pparser
from KD_tree import construct_kd_tree
from Protein import Protein

dimensions = 10

def main():
	folder = "PDBfiles/"
	Protein_dict = pparser.parse_proteins(folder)
	kdtree = construct_kd_tree(Protein_dict, 10)
	print (kdtree.toJson())
	print(kdtree.nearest_neighbor((0 , 0 , 0 , 0 , 0 , 0 , 2 , 0.16981132075471697 , 2 , 0.02358490566037736)))


	
if __name__ == "__main__":
	main()
