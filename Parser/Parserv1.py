#My attempt at a basic Python-based Parser. Will take in ASCII text and reorganize based on input.
import argparse


parser = argparse.ArgumentParser()

#arguments
parser.add_argument("file", help = "stores file")
parser.add_argument("--sort", help = "alphabetize", default = False, action = "store_true")
parser.add_argument("--reverse", "-r", help = "reverses input", default = False, action = "store_true")

args = parser.parse_args()
if args.file.endswith('.txt'):
	wordSortList = []
	with open(args.file) as file:
	    for line in file:
        	wordSortList.append(line)
else:
	wordSortList = args.file.split()

print("apple")


if args.sort:
	sorted(wordSortList)

if args.reverse:
	wordSortList.reverse()

for a in wordSortList:
	print(a)





