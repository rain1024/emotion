class Emotion:
    def __init__(self, name, en=None, emoji=None):
        self.name = name
        self.en = en
        self.emoji = emoji
        self.trigger = None
        self.physical = None
        self.term = None
        self.levels = []
        if self.name == "tin tưởng":
            self.levels = ["tán thành", "tin tưởng", "ngưỡng mộ"]

    def display(self):
        print("=======================")
        if self.term:
            print(f"-> {self.term}")
        print(self.name)
        print(self.en)
        print(self.emoji)
        print("# Trigger")
        print(self.trigger)
        print("\n# Physical")
        print(self.physical)
        if len(self.levels) > 0:
            print("\n# Levels")
            print(" > ".join(self.levels))
