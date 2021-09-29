class Blobservation:

    def __init__(self, h, w=0):
        self.h = h
        self.w = w if w else h
        self.population = []

    def populate(self, population):
        new_population = self.population.copy()
        for blob in population:
            x, y, size = blob['x'], blob['y'], blob['size']
            if type(x) != int or x < 0 or x >= self.h or type(y) != int or y < 0 or y >= self.w or type(size) != int or size < 1:
                raise ValueError
            new_population.append([x, y, size])
        self.population = new_population
        self.consume()

    def consume(self):
        new_population = []
        for blob in self.population:
            fuse_index = None
            for new_blob in new_population:
                if blob[0] == new_blob[0] and blob[1] == new_blob[1]:
                    fuse_index = new_population.index(new_blob)
                    break
            if fuse_index is not None:
                new_population[fuse_index][2] += blob[2]
            else:
                new_population.append(blob)
        self.population = new_population

    def targets(self, blob):
        return [target for target in self.population if target[2] < blob[2]]

    @staticmethod
    def distance_and_dir(blob, targets):
        distances = [max(abs(blob[0] - target[0]), abs(blob[1] - target[1])) for target in targets]
        closest = min(distances)
        targets = [target for i, target in enumerate(targets) if distances[i] == closest]
        sizes = [target[2] for target in targets]
        targets = [target for target in targets if target[2] == max(sizes)]
        clock = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
        directions = [[(blob[0] < target[0]) - (blob[0] > target[0]), (blob[1] < target[1]) - (blob[1] > target[1])]
                      for target in targets]
        clock_directions_indexes = [clock.index(directions[i]) for i, target in enumerate(targets)]
        return directions[clock_directions_indexes.index(min(clock_directions_indexes))]

    def move(self, steps=1):
        if type(steps) != int or steps < 1:
            raise ValueError
        for step in range(steps):
            new_population = []
            for blob in self.population:
                targets = self.targets(blob)
                if targets:
                    direction = self.distance_and_dir(blob, targets)
                    new_population.append([blob[0]+direction[0], blob[1]+direction[1], blob[2]])
                else:
                    new_population.append(blob)
            self.population = new_population.copy()
            self.consume()

    def print_state(self):
        return sorted(self.population)