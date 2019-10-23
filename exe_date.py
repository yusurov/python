#!/usr/bin/env python3

from datetime import datetime
from math import sqrt
from argparse import ArgumentParser
import sys

def output_to(path, content):
        if path:
                with open(path, 'a+') as f:
                        f.write(content)
        else:
                print("content")

parser = ArgumentParser(description="racine caree")
parser.add_argument('-i', '--integer', required=True, type=int, nargs=1)
parser.add_argument('-o', '--output')

args = parser.parse_args()
try:
	
	racine = (sqrt(args.integer[0]))
	now_date = str(datetime.now())
	result_str = "{date} : {result}\n".format(date=now_date, result=racine) 
	output_to(args.output, result_str)
except ValueError:
	print("integer must be positive")
	sys.exit(-1)
