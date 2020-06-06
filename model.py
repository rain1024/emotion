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
        self.synonym = set()
        if self.name == "tin tưởng":
            self.levels = ["tán thành", "tin tưởng", "ngưỡng mộ"]

    def add_synonym(self, term):
        self.synonym.add(term)

    def display(self):
        print("=" * 80)
        if self.term:
            print(f"-> {self.term}")
        print(self.name.upper())
        print(self.en)
        print(self.emoji)
        print("# Trigger")
        print(self.trigger)
        print("\n# Physical")
        print(self.physical)
        print("\n# Synonym")
        print(", ".join(self.synonym))
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
