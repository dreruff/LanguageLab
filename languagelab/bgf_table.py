import source

class bgf_table(object):
  """docstring for bgf_table"""
  
  def __init__(self):
    self.table = list() #list of adjectival bi-grams
    self.count = dict() #frequency of adjectival bi-grams

  """Adds sourceline to end of list"""
  def append(self, source):
    self.table.append(source)
    self.increment_table(source.get_gram())

  """Increments frequency table"""
  def increment_table(self, bigram):
    if bigram in self.count:
      self.count[bigram] += 1
    else:
      self.count[bigram] = 1

  """Prints results into file filenameresult. File located in same directory as input file."""
  def get_table(self, filename):
    result = open('%sresult' % filename, 'w')

    for sourceline in self.table:
      result.write( sourceline.to_string() + '\n')

    for bigram, num in self.count.items():
      result.write('{0} : {1} \n'.format(bigram, num))
    
    result.close()
    