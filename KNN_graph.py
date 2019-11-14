
class D_G_node:
    """This class can be used to build any kind of directed graph this 
    class should only be used when defining another class"""
    def __init__(self, Object, neighbours=[]):
        self.info = Object
        self.neighbours=[]
        self.add_neighbours(neighbours)
        
    def set_neighbours(self, neighbours):
        for n in neighbours:
            if type(n) != D_G_node:
                raise NameError("Directed graph nodes neighbours "+
                "must also be directed graph nodes.")
        self.neighbours = neighbours 
    
    def get_neigbours(self):
        return(self.neighbours)
    
    def get_info(self):
        return(self.info)


class K_NN_Graph:
    """ This is a class implementation of a k nearest neighbour class, 
    wich is a directed graph in wich a node p is conected to another, q
    if and only if q is one of the k nearest neighbours of p."""
    
    def __init__(self, k, list_of_objects = False, 
    distance_function = Protein.distance, distance_matrix = False):
        
        self._k = k # Set k as semiprivate because can contain 
                    # interesting information for the user but should 
                    # not be changed outside the class.
        self.nodes = dict() # Using a dictionary we guaranty beeing able
                          # to find the node of interest in linear time.
        self.dist_fun = distance_function
        self.dist_mat = distance_matrix
        if list_of_objects:
			self.add_nodes(list_of_objects)
    
    
    def add_nodes(self, objects, new_distance_matrix = False):
		for obj in objects:
            self.nodes[obj] = D_G_node(obj)
            
        if new_distance_matrix:
			self.dist_mat = new_distance_matrix 
        self.build_graph()  

    
    def get_k_nearest_nodes(self, target):
		"""Returns the k most similar objects to the given target"""
		try:
			node = self.nodes[target]
		except:
			print("WARNING: Target not in the graph, adding it now.")
			self.add_nodes((target,))
			node = self.nodes[target]
		finally:
			neighbours = node.get_neigbours()
			neig_info = []
			for n in neighbours:
				neig_info.append(n.get_info)
		return neig_info
		
		
    def self.build_graph():
        print("Work in process")   
        # distance function stored in dist_fun, distance matrix in 
        # dist_mat and unconnected nodes in the dictionary nodes
