import pandas as pd
import pdb

class Info:

    def __init__(self, data_path):
        data = pd.read_csv(data_path, encoding='utf8')

    def setNrArticles(self, data):
        self.nr_articles = len(data)
        self.empty_articles = len(data[data.body.isnull()])





