from copy import copy

from datasets import datasets
import pandas as pd

from model import Emotion

df = pd.read_excel("data/emotions.xlsx")
df.fillna("", inplace=True)
datasets = list(df.T.to_dict().values())

words = {}
emotions = []
for item in datasets:
    emotion = Emotion(item["name"], item["en"], item["emoji"])
    emotion.trigger = item["trigger"]
    emotion.physical = item["physical"]
    emotions.append(emotion)

for emotion in emotions:
    words[emotion.name] = emotion

df_synonym = pd.read_excel("data/synonym.xlsx")
synonym = list(df_synonym.T.to_dict().values())
synonym_words = {}
for item in synonym:
    word1 = item["word1"]
    word2 = item["word2"]
    if word2 not in words:
        raise Exception(f"Cannot map term {word2}")
    synonym_words[word1] = words[word2]

df_levels = pd.read_excel("data/levels.xlsx")
levels = list(df_levels.T.to_dict().values())
for item in levels:
    word1 = item["word1"]
    word2 = item["word2"]
    score = item["score"]
    if word2 not in words:
        raise Exception(f"Cannot map term {word2}")

def get_all():
    return emotions


def find(term):
    for emotion in emotions:
        if emotion.name == term or emotion.en == term or emotion.emoji == term:
            return emotion
    if term in synonym_words:
        item = copy(synonym_words[term])
        item.term = term
        return item
    return None
