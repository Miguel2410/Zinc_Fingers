import numpy 

class Protein:

   def __init__(self, name, C2H2, C2WH2,GATA3, CCHC, ZN2C6, zinc, prot_len, pos, num_chain, hys_cys):
      self.name = name
      self.C2H2 = C2H2  #0/1
      self.C2WH2 = C2WH2 #0/1
      self.GATA3 = GATA3 #0/1
      self.CCHC = CCHC #0/1
      self.ZN2C6 = ZN2C6 #0/1
      self.zinc = zinc #0/1/2 
      self.prot_len = prot_len 
      self.pos = pos  # Numeric, between 0 and 1
      self.num_chain = num_chain 
      self.hys_cys = hys_cys  # Numeric, between 0 and 1


   def distance(self, protein_2):
      """ We are going to use Manhattan distance, since Euclidean distance breaks in high dimensionality data"""

      spatial_pos = [self.C2H2, self.C2WH2, self.GATA3, self.CCHC, self.ZN2C6, self.zinc, self.prot_len, self.pos, self.num_chain, self.hys_cys]
      spatial_pos_2  = [protein_2.C2H2, protein_2.C2WH2, protein_2.GATA3, protein_2.CCHC, protein_2.ZN2C6, protein_2.zinc, protein_2.prot_len, protein_2.pos, protein_2.num_chain, protein_2.hys_cys]
      manhattan_distance = sum(abs(spatial_pos_2 - spatial_pos))
      return manhattan_distance

   