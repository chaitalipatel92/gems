###FOR FURTHER INSTRUCTIONS PLEASE REFER TO alternateresidues.py SAMPLE FILE
###SAMPLE COMMAND :
# python unknownheavyatoms.py -libs "gmml/dat/lib/GLYCAM_amino_06h.lib","gmml/dat/lib/GLYCAM_aminoct_06h.lib","gmml/dat/lib/GLYCAM_aminont_06h.lib" -prep "gmml/dat/prep/Glycam_06.prep" -pdb "gmml/example/pdb/sucros.pdb"

import gmml
import sys

temp = gmml.PdbPreprocessor()
libs = gmml.string_vector()
prep = gmml.string_vector()

for i, arg in enumerate(sys.argv):	
    if arg == '-libs':                       
		arguments = sys.argv[i+1].split(',')
		for argument in arguments:
			libs.push_back(argument)
    elif arg == '-prep':
		arguments = sys.argv[i+1].split(',')
		for argument in arguments:
			prep.push_back(argument)
    elif arg == '-pdb':
		pdb = sys.argv[i+1]

temp.ExtractUnknownHeavyAtoms(pdb, libs, prep)	

###FOR GIVING THE FILES MANUALLY AND THROUGH THE COMMAND LINE USE THE FOLOWIG SECTION
#libs.push_back("gmml/dat/lib/GLYCAM_amino_06h.lib")
#libs.push_back("gmml/dat/lib/GLYCAM_aminoct_06h.lib")
#libs.push_back("gmml/dat/lib/GLYCAM_aminont_06h.lib")
#prep.push_back("gmml/dat/prep/Glycam_06.prep")
#temp.ExtractUnknownHeavyAtoms("gmml/example/pdb/sucros.pdb", libs, prep)

unrecognized_heavy_atoms = temp.GetUnrecognizedHeavyAtoms()
for x in xrange(0, unrecognized_heavy_atoms.size()):
        unrecognized_heavy_atoms[x].Print()

pdbfile = gmml.PdbFile(pdb)

temp.RemoveUnknownHeavyAtoms(pdbfile, unrecognized_heavy_atoms)

pdbfile.Write('sucros-unknownheavyatoms-update.pdb')

