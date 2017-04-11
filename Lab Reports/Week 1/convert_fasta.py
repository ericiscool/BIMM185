"""
Converts the FASTA header to a different format and prints the concatenated string
"""

"""
Do stuff
"""
import sys

with open('TCDB.faa') as f:
  file_str = f.read().split('\n')

print 'Read File'
print len(file_str)
for line in file_str:
  if line.startswith('>'):
    print
    parts = line.split('|')
    sys.stdout.write(str(parts[-1].split(' ')[0]))
    sys.stdout.write('-')
    sys.stdout.write(parts[2])
    sys.stdout.write('\t')
  else:
    sys.stdout.write(line.strip())

print
