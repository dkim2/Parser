#My attempt at a basic Python-based Parser. Will take in ASCII text and reorganize based on input.
#Based off of http://pythonpracticeprojects.com/command-line-parser.html
import argparse


parser = argparse.ArgumentParser()

#arguments
parser.add_argument("file", help = "stores file")
parser.add_argument("--sort", help = "alphabetize", default = False, action = "store_true")
parser.add_argument("--reverse", "-r", help = "reverses input", default = False, action = "store_true")
parser.add_argument("--output", "-o", nargs = '?', help = "Writes the line sorted contents to out_file", default = "No Output File Selected")

args = parser.parse_args()
if args.file.endswith('.txt'):
	wordSortList = []
	with open(args.file) as file:
	    for line in file:
        	wordSortList.append(line)
else:
	wordSortList = args.file.split()


if args.sort:
	wordSortList = sorted(wordSortList)

if args.reverse:
	wordSortList = wordSortList.reverse()

if args.output!= "No Output File Selected":
	file = open(args.output, 'r+')
	file.write(str(wordSortList) + "\n")
	print("Input has been written into output file.")


#Print Current state of input file
print("Printing current state of file")

for a in wordSortList:
	print(a)







