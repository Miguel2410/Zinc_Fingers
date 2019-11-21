import unittest

from Protein import Protein

class TestDistance(unittest.TestCase):
	def test_distance(self):
		# Test for all dimensions:

		# Protein Constructor:
		protein1 = Protein("SelfProt", 2, 0, 1, 1, 0, 0, 2, 0.15, 1, 0.076)
		#Protein(name, C2H2, C2WH2,GATA3, CCHC, ZN2C6, zinc, prot_len, pos, num_chain, hys_cys)

		# Test distance when protein 2 is correct:
		protein2 = Protein("CorrectProt", 1, 0, 0, 1, 0, 3, 2, 0.24, 2, 0.016)
		self.assertAlmostEqual(protein1.distance(protein2), 6.15)

		# Test distance when protein 2 is 0:
		protein2 = Protein("CorrectProt", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
		self.assertAlmostEqual(protein1.distance(protein2), 7.226)


	def test_values(self):
		protein1 = Protein("SelfProt", 2, 0, 1, 1, 0, 0, 2, 0.15, 1, 0.076)
		#Make sure errors are raised when necessary

		# Test distance when protein 2 has negative numbers

		protein2 = Protein("IncorrectProt", -3, 0, 0, 1, 0, 3, 2, 0.24, 2, 0.016)
		self.assertRaises(ValueError, protein1.distance, protein2 )

		# Test distance when protein 2 has booleans:
		protein2 = Protein("IncorrectProt", True, 0, 0, 1, 0, 3, 2, 0.24, 2, 0.016)
		self.assertRaises(ValueError, protein1.distance, protein2 )


		# Test distance when protein 2 has strings:
		protein2 = Protein("IncorrectProt", "twenty", 0, 0, 1, 0, 3, 2, 0.24, 2, 0.016)
		self.assertRaises(ValueError, protein1.distance, protein2 )


		# Test for K dimensions:

if __name__ == '__main__':
	unittest.main()