import math

class Node(object):
   
   def __init__(self , data=None , left=None , right=None):
      self.data = data
      self.left = left
      self.right = right

            
class KDNode(Node):
   
   def __init__(self , data=None , left=None , right=None , axis=0 , dimensions=None):
 
      super(KDNode , self).__init__(data , left , right)
      self.axis = axis
      self.dimensions = dimensions
   
   def add(self , point):
      
      current = self
      while True:
         
         if current.data is None:
            current.data = point
            return current
         
         if point[current.axis] < current.data[current.axis]:
            if current.left is None:
               return self.__class__(point ,axis=self.axis, dimensions=self.dimensions)
            else:
               current = current.left
         else:
            if current.right is None:
               return self.__class__(point ,axis=self.axis,  dimensions=self.dimensions)
            else:
               current = current.right

   def dist_ejes(self , point , axis):

      return math.pow(self.data[axis] - point[axis] , 2)
   
   def dist(self , point):

      r = range(self.dimensions)
      return sum([self.dist_ejes(point , i) for i in r])
   
