#!/usr/bin/env python3

#Changer: Fasta File Name Change (FFNC)
#This pyhon software will read the first line of a fasta file, search its first line and change its name acording to it with the diference of removing the ('>') ending at eh ','. It will also substitute the ' ' for a '_'.
#Version 1.0 - 10th Dezember, 2019
#
# Copyright © 2019 Lucas Jose Luduverio Pizauro
#
# FFNC is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# FFNC is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public
# License for more details.



import os
import argparse

def run(input, new_dir):
    original_file = open(input)
    header = original_file.readline()
    print(header)
    if header.startswith('>'):
        new_header = header.split(',')[0].replace('>', '').replace(' ', '_')
        print(new_header)
    
    #os.rename(input, new_header)
    with open(input, "rt") as old_file, open(new_dir + '/' + new_header + ".fa", "wt") as new_file:
        for line in old_file:
            new_file.write(line)
    
    

 #   if original_file != header:
     #   original = str(original_file)
     #   os.rename(original_file, header)
    #    
def main():
    parser=argparse.ArgumentParser(description="change the name of a fasta file to its first line")
    parser.add_argument("-in",help="fasta input file" ,dest="input", nargs='+', required=True)
    parser.add_argument("-nd", help="director for the exit fiel", dest="new_dir")
    args=parser.parse_args()

    if args.new_dir:
        os.mkdir(args.new_dir)
        new_dir = args.new_dir
    else:
        new_dir = '.'
    for file in args.input:
        run(file, new_dir)

if __name__=="__main__":
    main()

