class User:
    RANKS = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self):
        self.rank = -8
        self.progress = 0

    def add_points(self, points):
        self.progress += points
        if self.progress >= 100:
            if self.rank != 8:
                plus = int(self.progress/100)
                self.progress = self.progress % 100
                if self.RANKS.index(self.rank)+plus <= 15:
                    self.rank = self.RANKS[self.RANKS.index(self.rank)+plus]
                else:
                    self.rank = 8
        if self.rank == 8:
            self.progress = 0

    def inc_progress(self, rank):
        if rank not in self.RANKS:
            raise ValueError("Invalid input")
        if rank == self.rank:
            self.add_points(3)
        elif rank == self.rank - 1 or (rank == -1 and self.rank == 1):
            self.add_points(1)
        elif rank > self.rank:
            points = 10 * (self.RANKS.index(rank) - self.RANKS.index(self.rank))**2
            self.add_points(points)