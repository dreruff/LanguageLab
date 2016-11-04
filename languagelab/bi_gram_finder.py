import sys
import scanner
import dictionary
import bgf_table

class bi_gram_finder:
  """docstring for simple_gram_finder"""

  """Initializes bi_gram_finder table and adjective dictionary"""
  def __init__(self, filename):
    self.bgf_table = bgf_table.bgf_table() #list of valid bigrams
    self.dictionary = dictionary.dictionary("../dictionary.txt") #dictionary of adjectives
    self.find_bi_grams(filename)

  """"""
  def find_bi_grams(self, filename):
    scan = scanner.scanner(filename)
    src = scan.get_sourcelist()
    for line in src:
      bigram = line.get_gram()
      if self.is_valid_bi_gram(bigram.split()):
        self.bgf_table.append(line)


  """Returns true if bigram is valid adjectival bigram, false otherwise"""
  def is_valid_bi_gram(self, bigram):
    for word in bigram:
      if not self.is_adjective(word):
        return False
    return True

  """Returns true if word is adjective, false otherwise"""
  def is_adjective(self, word):
    if not self.dictionary.contains(word):
      return False
    return True

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print "Please include file."
    print "python n_gram_finder.py filename"
    sys.exit()
  
  filename = sys.argv[1]
  
  bgf = bi_gram_finder(filename)
  bgf.bgf_table.get_table(filename)
