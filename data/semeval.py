import shutil
import os
import itertools
import shlex
import re
import string

"""
Utility functions for processing SemEval data sets into suitable form for ESN.

**NOTE** This is WILDLY INEFFICIENT code, it is merely a quick hack to get the
data in the form that I want it. If processing larger data sets, should definitely
rewrite since each function basically reads through an entire file, writes to a 
temp file, and then copies the temp file. 

"""

def remove_blank_lines(filename):
    with open(filename, 'r') as in_file:
        with open("temp.txt", 'w') as temp:
            for line in in_file:    
                if line.rstrip():
                    temp.write(line)
    # inefficient, but couldn't get r+ to work:
    shutil.copyfile("temp.txt", filename)
    os.remove("temp.txt")
    
def get_causal_sents(filename):
    with open(filename, 'r') as in_file:
        with open("temp.txt", 'w') as out_file:
            while True:
                next3lines = list(itertools.islice(in_file, 3))
                if not next3lines:
                    break
                if "Cause-Effect" in next3lines[1]:
                    first_line = shlex.split(next3lines[0])
                    out_file.write("1 " + first_line[1] + '\n') # positive classification + sentence
    shutil.copyfile("temp.txt", filename)
    os.remove("temp.txt")
    
def get_other_sents(filename):
    with open(filename, 'r') as in_file:
        with open("temp.txt", 'w') as out_file:
            while True:
                next3lines = list(itertools.islice(in_file,3))
                if not next3lines:
                    break
                if "Cause-Effect" not in next3lines[1]:
                    first_line = shlex.split(next3lines[0])        
                    out_file.write("0 " + first_line[1] + '\n') # negative classification + sentence
    shutil.copyfile("temp.txt", filename)
    os.remove("temp.txt")
    
def contains_digits(sent):
    d = re.compile('\d')
    return bool(d.search(sent))   
    
def select_other_sents(filename, num_sents):
    with open(filename, 'r') as in_file:
        with open("temp.txt", 'w') as out_file:
            count = 0
            while (count < num_sents):
                line = in_file.readline().split()
                del line[0]
                sent = ' '.join(line)
                # only select lines that do not have integer values in them:
                if not contains_digits(sent):
                    out_file.write("0 " + sent + '\n')
                    count = count + 1
    shutil.copyfile("temp.txt", filename)
    os.remove("temp.txt")
                    
def remove_tags(filename):
    with open(filename, 'r') as in_file:
        with open("temp.txt", 'w') as out_file:
            for line in in_file:
                line = re.sub(r'<.*?>', '', line)
                line = line.translate(None, string.punctuation).lower()
                out_file.write(line)
    shutil.copyfile("temp.txt", filename)
    os.remove("temp.txt")                
                