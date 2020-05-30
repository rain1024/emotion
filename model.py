from termcolor import colored
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
        print("=" * 80)
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
            n = len(self.levels)
            s = ""
            for i, level in enumerate(self.levels):
                if level == self.name:
                    s += "{" + level + "}"
                else:
                    s += level
                if i != n - 1:
                    s += " > "
            print(s)

