import protein_parser as pparser
from KDTree import parse_protein_list, kd_tree, nearest_neighbor, delete_element, k_nearest_neighbors
import pprint


pp = pprint.PrettyPrinter(indent=4)

#for element in pparser.parse_proteins("/Users/miguel/Desktop/MASTER/APA/Zinc_Fingers/PDBfiles/"):
#	for element2 in pparser.parse_proteins("/Users/miguel/Desktop/MASTER/APA/Zinc_Fingers/PDBfiles/"):
#		print(element.name, element2.name, element.distance(element2))


dimensions = 10

def main():
   folder = "PDBfiles/"
   print ("Executing this file as main show:")
   proteinas = pparser.parse_proteins(folder)
   coords = parse_protein_list(proteinas)
   #pp.pprint(coords)
   #coords_aux=[(1,3,'1'),(4,5,'2'),(0,4,'3'),(2,4,'4')]
   kdtree = kd_tree(coords, dimensions, depth=0)
   pp.pprint(k_nearest_neighbors(10,kdtree, (1,0,0,0,0,0,4,3,2,0.4),0,10))
   #pp.pprint(nearest_neighbor(kdtree , (0 , 0 , 0 , 0 , 0 , 0 , 2 , 0.16981132075471697 , 2 , 0.02358490566037736) , 0 ,10))
   #a_borrar=(3, 0, 0, 0, 0, 0, 0, 0.3111111111111111, 3, 0.14444444444444443, '1aay')
   #pp.pprint(kdtree.toJson())
   #delete_element(kdtree,a_borrar)

   
if __name__ == "__main__":
   main()
   parse_protein_list(pparser.parse_proteins("PDBfiles/"))