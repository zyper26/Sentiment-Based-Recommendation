import numpy as np
import pandas as pd
import pickle

class Recommendation:
    def __init__(self):
        self.logit =pickle.load(open('pickle/logistic_model.pkl', 'rb'))
        self.word_vectorizer = pickle.load(open('pickle/word_vectorizer.pkl', 'rb'))
        self.user_predicted_ratings = pd.read_pickle("pickle/user_predicted_ratings.pkl")
        self.df = pd.read_csv("processed_data.csv")

    def top_5_recommendation(self, user_input):
        if (user_input in self.user_predicted_ratings.index):
            arr = self.user_predicted_ratings.loc[user_input].sort_values(ascending=False)[0:20]
            pred = {}
            
            for prod_name in list(arr.index):
                product = prod_name
                product_name_review_list = list(self.df[self.df['name']== product]['reviews_title_and_text'])
                features= self.word_vectorizer.transform(product_name_review_list)
                self.logit.predict(features)
                pred[product] = self.logit.predict(features).mean()*100
            
            result= pd.Series(pred).sort_values(ascending = False).head(5).index.tolist()
            return result
        else:
            return None