with open('expression_data.txt') as f:
  plain_str = f.read()
  conv_str = plain_str.replace(',', '\t')

with open('new.txt', 'w') as f:
  f.write(conv_str)
