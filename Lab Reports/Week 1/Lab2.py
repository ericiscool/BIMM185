
with open('RS_sorted.txt') as f:
  file_read = f.read().splitlines()

num_matches = dict()
max_match = dict()
names = set()
MAX_PROT = 2000

for ind,line in enumerate(file_read):

  if len(names) == MAX_PROT:
    break
  parts = line.split()
  num_matches[parts[0]] = 0
  max_match[parts[0]] = (float(parts[-1]), parts[1])
  names.add(parts[0])

names = set()
for ind,line in enumerate(file_read):
  if len(names) == MAX_PROT:
    break
  parts = line.split()
  num_matches[parts[0]] += 1
  max_match[parts[0]] = max(max_match[parts[0]], (float(parts[-1]), parts[1]))
  names.add(parts[0])


max_interactions = (-1,-1)
for key, val in num_matches.iteritems():
  max_interactions = max(max_interactions, (val,key))

  print key, '\t', max_match[key][1], '\t', val, '\t', max_match[key][0]
  '''
  print 'Protien: ', key
  print '\t Has %d matches' % val
  print '\t Best match is with: ', max_match[key][1], ' with value ', max_match[key][0]
  '''


print max_interactions
