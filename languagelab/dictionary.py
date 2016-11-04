class dictionary():
  """docstring for Dictionary"""

  def __init__(self, filename = 'dictionary.txt'):
    self.words = set()
    for line in open(filename, 'r'):
      self.words.add(line.strip())

  def contains(self, word):
    return word in self.words
