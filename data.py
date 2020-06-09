from copy import copy
import pandas as pd

from model import Emotion

df = pd.read_excel("database/emotions.xlsx")
df.fillna("", inplace=True)
datasets = list(df.T.to_dict().values())

words = {}
emotions = []
for item in datasets:
    emotion = Emotion(item["name"], item["en"], item["emoji"])
    emotion.definition = item["definition"]
    emotion.physiology = item["physiology"]
    emotion.behavior = item["behavior"]
    emotion.action = item["action"]
    emotion.note = item["note"]
    emotions.append(emotion)

for emotion in emotions:
    words[emotion.name] = emotion



class Synonym:
    @staticmethod
    def init():
        df_synonym = pd.read_excel("database/synonym.xlsx")
        synonym = list(df_synonym.T.to_dict().values())
        terms = {}
        for item in synonym:
            term = item["term"]
            class_ = item["class"]
            if class_ not in words:
                raise Exception(f"Cannot map term {class_}")
            emotion = words[class_]
            emotion.add_synonym(term)
            terms[term] = emotion
        Synonym.terms = terms

    @staticmethod
    def find(term):
        if term in Synonym.terms:
            item = copy(Synonym.terms[term])
            item.term = term
            return item
        return None

Synonym.init()

class Levels:
    @staticmethod
    def init():
        df_levels = pd.read_excel("database/levels.xlsx")
        levels = list(df_levels.T.to_dict().values())
        for item in levels:
            term = item["word"]
            class_ = item["class"]
            score = item["score"]
            if class_ not in words:
                raise Exception(f"Cannot map term {class_}")
            emotion = words[class_]
            emotion.add_level(term, score)
        pass

    @staticmethod
    def find(term):
        pass

Levels.init()


class Emotions:
    @staticmethod
    def find(term: str) -> Emotion:
        for emotion in emotions:
            if emotion.name == term or emotion.en == term or emotion.emoji == term:
                return emotion
        return Synonym.find(term)