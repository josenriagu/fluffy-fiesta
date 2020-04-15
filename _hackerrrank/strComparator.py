class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        pass
    
    # In short, when sorting in ascending order, a comparator function returns -1 if a < b, 0  if a = b, and 1 if a > b.
    # reverse is the case for descending order

    def comparator(self, a, b):
        # sort score in descending
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        # sort name in ascending
        elif a.name > b.name:
            return 1
        return -1


print("amy" > "david")
print("david" > "amy")
