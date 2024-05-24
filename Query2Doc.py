import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from Reader import ReadPDF
from JournalDataset import read_json, int_to_label

# @title <p> Make it into class
class Query2Doc:
  def __init__(self, data_path, mode='cosine'):
    self.data = read_json(data_path)
    self.reader = ReadPDF()
    self.vectorizer = TfidfVectorizer()
    
    self.texts = [(doc['filename'], doc['text']) for doc in self.data]
    self.doc_vector = self.vectorizer.fit_transform([text[0] for name, text in self.texts])
    
    mode_dict = {
        'cosine':self.cosine_similarites
    }
    self.mode = mode_dict[mode]

  def cosine_similarites(self, doc_vector, query_vector):
    cosine_similarities = cosine_similarity(query_vector, doc_vector).flatten()
    ranked_indices = np.argsort(cosine_similarities)[::-1]
    ranked_scores = cosine_similarities[ranked_indices]
    
    name_documents = [f'{self.data[i]["filename"]}' for i in ranked_indices]
    label_documents = [f'{int_to_label[self.data[i]["label"]]}' for i in ranked_indices]
    results = pd.DataFrame({
        'idx': ranked_indices,
        'Document': name_documents,
        'Label': label_documents,
        'Similarity Score': ranked_scores
    })
    
    return results

  def __call__(self, query):

    query_vector = self.vectorizer.transform([query])
    results =  self.mode(self.doc_vector, query_vector)

    return results
