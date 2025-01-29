class Boss:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.hits = []  # Sum of all hits against this boss
