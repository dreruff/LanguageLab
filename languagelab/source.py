class source():
  
  def __init__(self, gram, year, match_count, page_count ):
    self.gram = gram
    self.year = year
    self.match_count = match_count
    self.page_count = page_count

  def get_gram(self):
    return self.gram
    
  def get_year(self):
    return self.year
    
  def get_match_count(self):
    return self.match_count
    
  def get_page_count(self):
    return self.page_count

  def to_string(self):
    return '{0} {1} {2} {3}'.format(self.gram, self.year, self.match_count, self.page_count)
