import shutil
import os
import itertools
import shlex

"""

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
        with open("causal_sents.txt", 'w') as out_file:
            while True:
                next3lines = list(itertools.islice(in_file, 3))
                if not next3lines:
                    break
                if "Cause-Effect" in next3lines[1]:
                    first_line = shlex.split(next3lines[0])
                    out_file.write("1 " + first_line[1]) # positive classification + sentence
                    
                    # TODO: remove "e" tags from first_line