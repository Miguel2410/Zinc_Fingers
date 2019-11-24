# Zinc_Fingers

This program takes as input a PDB Folder, which contains PDB files inside. They are parsed and stored into a KD tree. 

v1 is for dirty initial code, as v2 is the final code and the one that should be used.

The usage is the next one

python3 main.py -PDBfolder {name of the folder} -test

This will give you a full demonstration of printing the kd tree plus printing the nearest neighbor for a dummy variable defined inside main, and the two nearest neighbors for a the same variable.

The nearest neighbor is computed through an algorithm that prunes the tree. The k nearest neighbors are computed by brute force.
