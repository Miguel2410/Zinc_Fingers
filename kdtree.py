

class Node:
	def __init__(self, id='', value=list()):
		self.id = id
		self.value = value
	
	def toJson(self):
		return {
			'id': self.id,
			'value' : self.value
		}
		
class KDNode:
	def __init__(self, left = None, right = None, root = Node(), dim=None, cutting_point=None):
		self.root = root
		self.left = left
		self.right = right
		self.dim = dim
		self.cut = cutting_point
	
	def toJson(self):
		
		return {
			'root': self.root.toJson(),
			'left': self.left.toJson() if self.left is not None else {},
			'right': self.right.toJson() if self.right is not None else {}
		}
	
	def k_nearest_neighbors(self, k , point , result=list()):
		if self.root is None:
			return None
		if (manhattan_distance(self.root.root.value , point) < k):
			result.append(self.root.root.id)
		
		k_nearest_neighbors(k , self.root.left , point , result)
		k_nearest_neighbors(k , self.root.right , point , result)
		
		return result
	
	def nearest_neighbor(self, , point , depth=0 , dimensions=10):
		
		if self.root is None:
			return None
		
		dim = depth % dimensions
		if point[dim] < int(self.root.value[dim]):
			next = self.left
			opposite = self.right
		else:
			next = self.right
			opposite = self.left
		
		closer = check_points_closer(point , nearest_neighbor(next , point , depth + 1 , 10) , self.root.value)
		
		if manhattan_distance(point , closer) > abs(point[dim] - self.root.value[dim]):
			closer = check_points_closer(point , nearest_neighbor(opposite , point , depth + 1 , 10) , closer)
		closer += (self.root.id ,)
		return closer
	
def parse_protein_list(proteins):
	coords = list()
	for element in proteins:
		coords.append(element.toTupple())
	return coords


def kd_tree (points,dimensions,depth=0):
	n = len(points)
	
	if n <= 0:
		return None

	dim = depth % dimensions
	sorted_points = sorted(points, key=lambda point: point[dim])
	mid = round(n/2)

	return KDNode(kd_tree (sorted_points[:mid], dimensions,  depth + 1 ), kd_tree (sorted_points[mid+1:], dimensions,  depth + 1 ), Node(sorted_points[mid][len(sorted_points[mid])-1],sorted_points[mid][0:len(sorted_points[mid])-1]))


def manhattan_distance(points1 , points2):
	distance = 0.0
	for x in range(len(points1) - 1):
		distance += abs(points1[x] - points2[x])
	return distance

def check_points_closer(point, p1, p2):
	
	if p1 is None:
		closer = p2
	else:
		if p2 is None:
			closer =  p1
		else:
			if manhattan_distance(point , p1) > manhattan_distance(point , p2):
				closer = p2
			else:
				closer = p1
	return closer

def delete_element_and_children(tree, point, depth=0, dimensions=10):
	dim = depth % dimensions

	if tree.root.id == point[len(point)-1]:
		tree.root = Node()
		tree.left = KDNode()
		tree.right = KDNode()
	else:
		if point[dim] < int(tree.root.value[dim]):
			delete_element_and_children(tree.left, point)
		else:
			delete_element_and_children(tree.right, point)
			
			
def nearest_neighbor(root, point, depth=0, dimensions=10):
	
	if root is None:
		return None

	dim = depth % dimensions
	if point[dim] < int(root.root.value[dim]):
		next = root.left
		opposite= root.right
	else:
		next = root.right
		opposite = root.left

	closer = check_points_closer(point, nearest_neighbor(next, point, depth + 1,10), root.root.value)

	if manhattan_distance(point, closer) > abs(point[dim] - root.root.value[dim]):
		
		closer = check_points_closer(point, nearest_neighbor(opposite, point, depth + 1,10), closer)
	closer += (root.root.id,)
	return closer


def k_nearest_neighbors(k, root, point,result=list()):
	if root is None:
		return None
	if(manhattan_distance(root.root.value, point) < k):
		
		result.append(root.root.id)
	
	k_nearest_neighbors(k, root.left, point, result)
	k_nearest_neighbors(k, root.right, point, result)

	return result



class KD_tree:
	
	def __init__(self, points,dimensions,depth=0):
		self.root = self.kd_tree (points,dimensions,depth=0)
	
	def kd_tree (self,points,dimensions,depth=0):
		n = len(points)
		
		if n <= 0:
			return None

		dim = depth % dimensions
		sorted_points = sorted(points, key=lambda point: point[dim])
		mid = round(n/2)

		return KDNode(kd_tree (sorted_points[:mid], dimensions,  depth + 1 ), kd_tree (sorted_points[mid+1:], dimensions,  depth + 1 ), Node(sorted_points[mid][len(sorted_points[mid])-1],sorted_points[mid][0:len(sorted_points[mid])-1]), dim, sorted_points[mid][dim])

		
	def group(self, x, d, k, *argv):
		dim = argv
		#print(dim)
		if dim == tuple():
			dim = list(range(len(x.__dict__.keys())))
		#print(dim)
		values= x.toTupple(*dim)
		min_d=[]
		for i in dim:
			min_d.append(0)
		valid_nodes = []
		valid_nodes = self.recursive_group(values, dim, min_d, self.root, d)
		print(valid_nodes)
		print(len(valid_nodes))
		return exhaustive_search(valid_nodes, k, d, *argv)
		
	def recursive_group(self,values, dimensions, min_d, node, max_d):
		if node is None or node.root is None:
			return tuple()
		print("max_d= ", max_d)
		dimention = node.dim
		valid_nodes = (node.root.id,)
		if dimention not in dimensions:
			#print("a")
			valid_nodes+=self.recursive_group(values, dimensions, min_d, node.left, max_d)
			valid_nodes+=self.recursive_group(values, dimensions, min_d, node.right, max_d)
		else:
			#print("b")
			mindistfor_d = values[dimention] - node.cut
			#print(mindistfor_d, dimention)
			#print("v",values[dimention], node.cut)
			if mindistfor_d < 0:
				valid_nodes+=self.recursive_group(values, dimensions, min_d, node.right, max_d)
				mindistfor_d = -mindistfor_d
				if mindistfor_d > min_d[dimention]:
					#print("baa")
					min_d[dimention] = mindistfor_d
				if sum(min_d)<max_d:
					#print("bab")
					valid_nodes+=self.recursive_group(values, dimensions, min_d, node.left, max_d)
			else:
				valid_nodes+=self.recursive_group(values, dimensions, min_d, node.left, max_d)
				if mindistfor_d > min_d[dimention]:
					min_d[dimention] = mindistfor_d
				if sum(min_d)<max_d:
					#print("bbb")
					valid_nodes+=self.recursive_group(values, dimensions, min_d, node.right, max_d)
		return valid_nodes
	
	def exhaustive_search(self, valid_nodes, k, d, *argv):
		print("""if the exhaustive search was done at the same time as the recursive group the efficiency could improve.
		(if found k neighbors at d< max_d the next neighbour to accept must be replacing the further apart from one from
		the already chosen -> we can reduce max_d to max(dist(point, accepted_neighbors)))""")
