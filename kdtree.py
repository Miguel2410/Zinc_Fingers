import pprint

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
	def __init__(self, left = None, right = None, root = Node()):
		self.root = root
		self.left = left
		self.right = right
	
	def toJson(self):
		
		return {
			'root': self.root.toJson(),
			'left': self.left.toJson() if self.left is not None else {},
			'right': self.right.toJson() if self.right is not None else {}
		}
		
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
			
def restore_tree(tree):
	list_elements = list()
	if tree.left is not None:
		restore_tree(tree.left)
	if tree.right is not None:
		restore_tree(tree.right)
	
def delete_element(tree, point, depth=0, dimensions=10):
	dim = depth % dimensions
	if tree is None:
		return None
	
	if tree.root.id == point[len(point)-1]:
		
		tree.root = Node()
	else:
		if point[dim] < int(tree.root.value[dim]):
			delete_element(tree.left, point)
		else:
			delete_element(tree.right, point)
			
			
def nearest_neighbor(root, point, depth=0, dimensions=10, list =list()):
	
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


def k_nearest_neighbors(k, root, point, depth=0, dimensions=10, result=list()):
	if root is None:
		return None
	if(manhattan_distance(root.root.value, point) < k):
		
		result.append(root.root.id)
	
	k_nearest_neighbors(k, root.left, point, result)
	k_nearest_neighbors(k, root.right, point, result)

	return result