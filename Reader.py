# Import Dependencies
import re, nltk

nltk.download('punkt')
nltk.download('stopwords')
from nltk import sent_tokenize, word_tokenize
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords

from autocorrect import Speller
from pypdf import PdfReader
from autocorrect import Speller

# @title <p> Make a reader class
class ReadPDF:
  def __init__(self, **kwargs):
    self.speller = Speller(lang='en')
    self.stemmer = LancasterStemmer()
    self.stopwords = stopwords.words('english')
    self.tokenizer = word_tokenize
  
  def preprocess(self, doc):
    words = self.tokenizer(doc)
    words_tok = list()

    for s in words:
        s = s.strip().lower() 
        s = s.replace("\n", " ") 
        s = re.sub(r'[^a-zA-Z. ]', ' ', s) 
        s = s.replace('  ', ' ')
        
        words_tok.append(s)

    return " ".join(words_tok)
  
  def autocorrect(self, doc):
    return ' '.join(self.speller(s) for s in doc.split())
  
  def remove_stopwords(self, doc):
    return " ".join([word for word in doc.split() if word not in self.stopwords])
  
  def stem(self, doc):
    return ' '.join(self.stemmer.stem(s) for s in doc.split())

  def read(self, 
           filepath:str, 
           preprocess=True, 
           remove_stopwords=True,
           stem=False,
           ):
    self.reader = PdfReader(filepath)

    results = []

    for page in self.reader.pages:
      # Extract the text from each pages
      result = page.extract_text()

      # Preprocess tht text (Remove symbols, casfolding)
      result = self.preprocess(result) if preprocess else result

      # Autocorrect using spell checker
      result = self.autocorrect(result)

      # Remove Stopwords
      result = self.remove_stopwords(result) if remove_stopwords else result

      # Stem if needed
      result = self.stemmer.stem(result) if stem else result

      results.append(result)
    
    return results