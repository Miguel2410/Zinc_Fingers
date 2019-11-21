from Protein import Protein

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
		
		if self.root is None:
			return None
		
		dim = depth % dimensions

		if coords[dim] < self.root[1].toTupple()[dim]:
			next = self.left
			opposite = self.right
		else:
			next = self.right
			opposite = self.left


		"""
		try:
			closer = check_points_closer(coords , next.nearest_neighbor(coords , depth + 1 , 10) , self.root[1])
		except:
			closer = check_points_closer(coords , opposite.nearest_neighbor(coords , depth + 1 , 10) , closer)
		"""

		closer += (self.root[0] ,)
		return closer





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
		
