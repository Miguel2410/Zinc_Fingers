
class Protein:

   def __init__(self, name, C2H2, C2WH2,GATA3, CCHC, ZN2C6, zinc, prot_len, pos, num_chain, hys_cys):
      self.name = name
      self.C2H2 = C2H2
      self.C2WH2 = C2WH2
      self.GATA3 = GATA3
      self.CCHC = CCHC
      self.ZN2C6 = ZN2C6
      self.zinc = zinc
      self.prot_len = prot_len
      self.pos = pos
      self.num_chain = num_chain
      self.hys_cys = hys_cys


   def get_atributes(self, *args):
	   keys=[x for x in self.__dict__.keys() if x in args]
	   values=[ self.__dict__[key] for key in keys]
	   return values
   
   def distance(self, protein_2, *args):

      if args==tuple():
         args = [x for x in self.__dict__.keys() if x not in ("name","__init__","get_atributes", "distance", "toTupple")]
      spatial_pos = self.get_atributes(*args)
      spatial_pos_2  = protein_2.get_atributes(*args)

      for element in spatial_pos:
         if isinstance(element, str):
            raise ValueError(str(element) + "is a string")
         if isinstance(element, bool):
            raise ValueError(str(element) + "is a boolean")
         if element < 0:
            raise ValueError(str(element) + "is negative")
   
      for element in spatial_pos_2:
         if isinstance(element, str):
            raise ValueError(str(element) + "is a string")
         if isinstance(element, bool):
            raise ValueError(str(element) + "is a boolean")
         if element < 0:
            raise ValueError(str(element) + "is negative")

      subs = ([a - b for a, b in zip(spatial_pos, spatial_pos_2)])
      abs_list = [abs(ele) for ele in subs] 
      manhattan_distance = sum(abs_list)
      return manhattan_distance


   def toTupple(self):
      return (self.C2H2, self.C2WH2, self.GATA3, self.CCHC, self.ZN2C6, self.zinc, self.prot_len, self.pos,self.num_chain,self.hys_cys)

      
      

