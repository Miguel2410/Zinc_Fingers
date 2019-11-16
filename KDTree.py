import math

class Node(object):
   
   def __init__(self , data=None , left=None , right=None):
      self.data = data
      self.left = left
      self.right = right
   
         
class KDNode(Node):
   
   def __init__(self , data=None , left=None , right=None , axis=0 , sel_axis=None , dimensions=None):
 
      super(KDNode , self).__init__(data , left , right)
      self.axis = axis
      self.sel_axis = sel_axis or (lambda prev_axis: (prev_axis+1) % dimensions)
      self.dimensions = dimensions
   
   def add(self , point):
      
      current = self
      while True:
         
         if current.data is None:
            current.data = point
            return current
         
         if point[current.axis] < current.data[current.axis]:
            if current.left is None:
               current.left = current.create_subnode(point)
               return current.left
            else:
               current = current.left
         else:
            if current.right is None:
               current.right = current.create_subnode(point)
               return current.right
            else:
               current = current.right
   
   def create_subnode(self , data):
      
      return self.__class__(data ,axis=self.sel_axis(self.axis) ,
                            sel_axis=self.sel_axis ,
                            dimensions=self.dimensions)

   def dist_ejes(self , point , axis):

      return math.pow(self.data[axis] - point[axis] , 2)
   
   def dist(self , point):

      r = range(self.dimensions)
      return sum([self.dist_ejes(point , i) for i in r])
   
