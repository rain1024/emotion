class Emotion:
    def __init__(self, name, en=None, emoji=None):
        self.name = name
        self.en = en
        self.emoji = emoji
        self.definition = None
        self.physical = None
        self.behavior = None
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
                self.levels.insert(i-1, (term, score))
                return
            i += 1
        self.levels.append((term, score))

    def display(self):
        print("=" * 80)
        if self.term:
            print(f"-> {self.term}")
        print(self.name.upper())
        print(self.en)
        if self.emoji:
            print(self.emoji)
        print("\n# Định nghĩa")
        if self.definition:
            print(self.definition)
        else:
            print("TBD")
        if self.physiology:
            print("\n# Phản ứng sinh lý học")
            print(self.physiology)
        if self.behavior:
            print("\n# Hành vi quan sát được")
            print(self.behavior)
        if self.action:
            print("\n# Hành động")
            print(self.action)
        if self.note:
            print("\n# Ghi chú")
            print(self.note)
        print("\n# Đồng nghĩa")
        print(", ".join(self.synonym))
        if len(self.levels) > 0:
            print("\n# Cấp độ")
            n = len(self.levels)
            s = ""
            for i, level in enumerate(self.levels):
                if level == self.name:
                    s += "{" + level[0] + "}"
                else:
                    s += level[0]
                if i != n - 1:
                    if i > 1:
                        if self.levels[i][1] == self.levels[i+1][1]:
                            s += ", "
                        else:
                            s += " > "
                    else:
                        s += " > "
            print(s)