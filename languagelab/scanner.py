import sys
import source

class scanner():
  def __init__(self, filename):
    self.source_list = list()
    try:
      for line in open(filename, 'r'):
        data = line.strip().lower().split()
        ngram = '{0} {1}'.format(data[0], data[1])
        year = data[2]
        match_count = data[3]
        page_count = data[4]
        src = source.source(ngram, year, match_count, page_count)
        self.source_list.append(src)
    except IOError as e:
      #file not found
      print "I/O error({0}): {1}".format(e.errno, e.strerror)
      sys.exit()
    
  def get_sourcelist(self):
    return self.source_list
