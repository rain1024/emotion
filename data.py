from datasets import datasets
import pandas as pd

df = pd.read_excel("data/emotions.xlsx")
df.fillna("", inplace=True)
datasets = list(df.T.to_dict().values())


class Emotion:
    def __init__(self, name, en=None, emoji=None):
        self.name = name
        self.en = en
        self.emoji = emoji
        self.trigger = None
        self.physical = None

    def display(self):
        print(self.name)
        print(self.en)
        print(self.emoji)
        print("# Trigger")
        print(self.trigger)
        print("\n# Physical")
        print(self.physical)


emotions = []
for item in datasets:
    emotion = Emotion(item["name"], item["en"], item["emoji"])
    emotion.trigger = item["trigger"]
    emotion.physical = item["physical"]
    emotions.append(emotion)


def get_all():
    return emotions


def find(term):
    for emotion in emotions:
        if emotion.name == term or emotion.en == term or emotion.emoji == term:
            return emotion
    return None
