import os
from pprint import pprint

import pandas as pd

os.system('clear')
directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/file'
place = 3

df = pd.read_csv(path,header=None)
words = df.stack()
words = words.str.split().explode()
words_count = words.value_counts()
word_count_df = words_count.reset_index()
word_count_df.columns = ['word','count']

nth_place = word_count_df.loc[place-1,'count']

top_three_df = word_count_df[word_count_df['count'] >= nth_place ]
print(top_three_df)