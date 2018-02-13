# Sprint1: process.py Code
# Danai Avgerinou, Ting Ting Liu, Shannon McNish, Jose A. Rodilla, Kerem Turgutlu
# Group Name: Bowbowbowbowsquaddd

import json
import os
import sys

# definitions
prefix = sys.argv[1]
check_dir = '/srv/runme/'

print("starting process.py now!")

#get files under check_dir directory
files = os.listdir(check_dir)
print(files)

#check files that begin with prefix
n = len(prefix)
good_files = [f for f in files if f[:n] == prefix]
name_age = ''
print(good_files)

#open every file
for file in good_files:
    print 'reading {}...\n'.format(check_dir + file)
    with open(check_dir + file) as f:
        #try:
        for line in f:
            try:
                d = json.loads(line)
                name = d['name']
                age = d['prop']['age']
                name_age += name + '\t' + str(age) + '\n'
            except:continue

# print 'Final Output\n'
# print name_age
with open(check_dir + prefix + '.txt', 'w+') as f:
    f.write(name_age)



