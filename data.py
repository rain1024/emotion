class Emotion:
    def __init__(self, name, en=None, emoji=None):
        self.name = name
        self.en = en
        self.emoji = emoji

    def display(self):
        print(self.name)
        print(self.en)
        print(self.emoji)


datasets = [
    ("buồn", "sad", ":("),
    ("vui", "happy", ":D")
]

emotions = []
for item in datasets:
    name, en, emoji = item
    emotion = Emotion(name, en, emoji)
    emotions.append(emotion)


def get_all():
    return emotions


def find(term):
    for emotion in emotions:
        if emotion.name == term or emotion.en == term or emotion.emoji == term:
            return emotion
    return None
