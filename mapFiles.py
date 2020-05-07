#!/usr/bin/env python3

import sys
import os

def main(root, file):
	out = open(file, 'w')
	map(root, out, 0)
	out.close()

def map(root, out, level):
	list = os.listdir(path=root)
	out.write("<ul>")
	for sub in list:
		if (sub[0] != '.'):
			out.write("<li>")
			fullPath = os.path.join(root, sub)
			if os.path.isdir(fullPath):
				indent(out, level)
				out.write(fullPath + "\n")
				map(fullPath, out, level + 1)
			else:
				indent(out, level)
				out.write("<a href=\"" + fullPath + "\">" + sub + "</a>\n")
	out.write("</ul>")

def indent(out, level):
	i = 0
	while i < level:
		out.write("\t")
		i += 1

if (len(sys.argv) == 3):
	main(sys.argv[1], sys.argv[2])
else:
	print("Two arguments required. The first is a root direcory; second is a output file")
