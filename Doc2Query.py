from collections import Counter
from Reader import ReadPDF

# @title <p> Make it into Class
class Doc2Query:
  def __init__(self, method='counter', query_len=20, **kwargs):
    self.reader = ReadPDF()
    self.query_len = query_len
    method_dict = {
      'counter':self.counter
    }
    self.method = method_dict[method]

  def check_word(self, word):
    if len(word) <= 2:
      return False
    if word in ['ieee', 'sic', 'fig', 'doi']:
      return False
    return True

  def counter(self, text):
    text = Counter([word for word in text[0].split() if self.check_word(word)]).most_common(self.query_len)
    query = ' '.join([word[0] for word in text])
    return query

  def __call__(self, doc_path):
    text_data = self.reader(doc_path)
    query = self.method(text_data)
    return query