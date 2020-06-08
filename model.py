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
        self.levels = [(name, 1)]

    def add_synonym(self, term):
        self.synonym.add(term)

    def add_level(self, term, score):
        min_s = self.levels[0][1]
        if score < min_s:
            self.levels.insert(0, (term, score))
            return
        i = 1
        for t, s in self.levels:
            if s > score:
                self.levels.insert(i, (term, score))
                return
            i += 1
        self.levels.append((term, score))

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
                    s += "{" + level[0] + "}"
                else:
                    s += level[0]
                if i != n - 1:
                    s += " > "
            print(s)