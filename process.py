from user_definition import *
import json
import os

#get files under check_dir directory
files = os.listdir(check_dir)

#check files that begin with prefix
n = len(prefix)
good_files = [f for f in files if f[:n] == prefix]

name_age = ''
#open every file
for file in good_files:
    print 'reading {}...\n'.format(check_dir + file)
    with open(check_dir + file) as f:
        try:
            for line in f:
                d = json.loads(line)
                name = d['name']
                age = d['prop']['age']
                name_age += name + '\t' + str(age) + '\n'
        except:continue

print 'Final Output\n'
print name_age

with open(check_dir + prefix + '.txt', 'w') as f:
    f.write(name_age)


