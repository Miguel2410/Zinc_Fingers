
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

   def distance(self, protein_2):
      print ("Work in process.")

      spatial_pos = [self.C2H2, self.C2WH2, self.GATA3, self.CCHC, self.ZN2C6, self.zinc, self.prot_len, self.pos, self.num_chain, self.hys_cys]
      spatial_pos_2  = [protein_2.C2H2, protein_2.C2WH2, protein_2.GATA3, protein_2.CCHC, protein_2.ZN2C6, protein_2.zinc, protein_2.prot_len, protein_2.pos, protein_2.num_chain, protein_2.hys_cys]
      manhattan_distance = sum(abs(spatial_pos_2 - spatial_pos))
      return manhattan_distance

   def toString(self):
      print(self.name + "  " +str(self.zinc) + " " +str(self.C2H2) + " "+ str(self.C2WH2) + " " + str(self.GATA3) + " " + str(self.prot_len)) 
      print(self.name + "  " +str(self.hys_cys))
      
   def distance(self, protein_2):
      print ("Work in process.")
