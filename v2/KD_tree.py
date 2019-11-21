from Protein import Protein

## SUPPORT FUNCTION #######
""" This funcion take a point and two extra points, and compute which one of P1 or P2 is nearer"""

def check_points_closer(point, p1, p2):
	
	if p1 is None:
		closer = p2
	else:
		if p2 is None:
			closer =  p1
		else:
			if p1.distance(point) > p2.distance(point):
				closer = p2
			else:
				closer = p1
	return closer


## KD TREE CLASES AND FUNCTIONS ###############


class KDNode:

	def __init__(self, left = None, right = None, root = None, dim=None, cutting_point=None):
		self.root = root
		self.left = left
		self.right = right
		self.dim = dim
		self.cut = cutting_point

	def toJson(self):
		"""This method is for visualizing purposes"""
		return {
			'root': self.root,
			'left': self.left.toJson() if self.left is not None else {},
			'right': self.right.toJson() if self.right is not None else {}
		}

	def nearest_neighbor(self, coords , depth=0 , dimensions=10):
		""" This function takes some coordinates, and give you the closest element after the KDtree has been modelled"""

		if self.root is None:
			return None
		
		dim = depth % dimensions

		if coords[dim] < self.root[1].toTupple()[dim]:
			next = self.left
			opposite = self.right
		else:
			next = self.right
			opposite = self.left

		if next is None:
			return None
		else:
			closer = check_points_closer(coords , next.nearest_neighbor(coords , depth + 1 , 10) , self.root[1])
		
		if closer.distance_to_coords(coords) > abs(coords[dim] - self.root[1].toTupple()[dim]):
			if opposite is None:
				return None
			else:
				closer = check_points_closer(coords , opposite.nearest_neighbor(coords , depth + 1 , 10) , closer)

		print ("the point closest is:", closer.name)
		return closer.name

def construct_kd_tree (Protein_list,dimensions,depth=0):
	n = len(Protein_list)

	if n <= 0: #If no proteins to store in the tree.
		return None

	dim = depth % dimensions
	sorted_points = sorted(Protein_list, key=lambda point: (point[1].toTupple())[dim])
	mid = round(n/2)

	return KDNode(construct_kd_tree (sorted_points[:mid], dimensions,  depth + 1 ), 
				  construct_kd_tree (sorted_points[mid+1:], dimensions,  depth + 1 ), 
				  (sorted_points[mid]))
		
