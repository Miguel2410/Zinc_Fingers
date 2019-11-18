
def parse_protein_list(proteins):
	coords = list()
	for element in proteins:
		coords.append(element.toTupple())
	return coords 


def kd_tree (points,dimensions,depth=0):
	n = len(points)

	if n <= 0:
		print ("Any points have been passed")
		return None

	dim = depth % dimensions
	sorted_points = sorted(points, key=lambda point: point[dim])
	mid = round(n/2)

	return {

		'root': sorted_points[mid][10],
		'left': kd_tree (sorted_points[:mid], dimensions,  depth + 1 ),
		'right': kd_tree (sorted_points[mid + 1:], dimensions,  depth + 1 )
	}

