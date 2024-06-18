# AnswerWithPaper

This project develops a system to extract and analyze textual data from PDF documents for identifying relevant documents in a corpus based on user input. The system preprocesses the extracted text by converting it to lowercase, removing punctuation and stopwords, and applying lemmatization. It then identifies the most common words in the document to form a query, which is transformed into a TF-IDF vector. This vector is compared against a pre-trained TF-IDF matrix of documents using cosine similarity. The system ranks the documents based on their relevance to the query, providing users with the most pertinent documents efficiently.

### Set up the environment using virtual environment
Make a new environment all install all the dependencies using this code in your terminal
```
python -m venv env
env/Scripts/activate
pip install requirements.txt
```

### Run the programs
You can change the config by change some parameters in main.py. Run the program using this code after you activate your env
```
python main.py
```

## Dataset
You can look at the [Drive Link](https://drive.google.com/file/d/1o5XbsEKuVt6HnxKx-rMM4K46UpJjvq0v/view) to see the dataset that use in program

## Colab Demo
You can also look at the [Colab Link](https://colab.research.google.com/drive/12pSBtUBWcZfe5XD5jdHZfCOgoRU9IPpd#scrollTo=0Qo1O13cRcb0) to see the program demo on colab

