# python 2

import difflib

# text1_lines = "atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaactgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatagcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc"
# text2_lines = "atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaactgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatagcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacattcgaccgtaaattgataatgaaatttacatgcttccgcgacgtttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgccgcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtatc"


###
### HERE IS WITH DATA TRANSFORMATION - RAW_DATA.splitlines()
###

print "\n-------------[ Printint Output with Transformation ]-------------\n"

# raw data
dna_seq_1 = "Sarah Seagrave"
dna_seq_2 = "Sarah Leslie Seagrave"

# data TRANSFORMATION
dna_seq_lines_1 = dna_seq_1.splitlines()
dna_seq_lines_2 = dna_seq_2.splitlines()

# declaring our method
the_method = difflib.Differ()

# running our method on the data
the_output = the_method.compare(dna_seq_lines_1, dna_seq_lines_2)

print '\n'.join(the_output)
print '\n'

###
### HERE IS WITH NO DATA TRANSFORMATION
###

print "\n-------------[ Printint Output without Transformation ]-------------\n"

# raw data
dna_seq_1 = "Sarah Seagrave"
dna_seq_2 = "Sarah Leslie Seagrave"

# declaring our method
the_method = difflib.Differ()

# running our method on the data
the_output = the_method.compare(dna_seq_1, dna_seq_2)

print '\n'.join(the_output)
print '\n'

###
### HERE IS DIFFLIB.HTML
###

function1 = ["Sarah Seagrave"]
function2 = ["Sarah Leslie Seagrave"]
differ = difflib.HtmlDiff()
differ.make_table(function1, function2)

print differ.make_file(function1, function2)
