#My attempt at a basic Python-based Parser. Will take in text and reorganize based on input.
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("sort", help = "file holder")
args = parser.parse_args()

print("apple")
with open(args.sort) as file:
    for line in file:
        print(line)
