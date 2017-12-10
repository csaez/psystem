import random


class Particle:
    def __init__(self):
        self.position = [0.0, 0.0]
        self.velocity = [0.0, 0.0]
        self.mass = 1.0


class PointEmitter:
    def __init__(self):
        self.position = [0.0, 0.0]
        self.rate = 20
        self.strength = 1.0

    def emit(self):
        for _ in range(self.rate):
            p = Particle()
            d = self.random_direction()
            for i in range(2):
                p.position[i] = self.position[i]
                p.velocity[i] = d[i] * self.strength
            yield p

    @staticmethod
    def random_direction():
        raw = [(2.0 * random.random()) - 1.0 for _ in range(2)]
        length = sum([x ** 2 for x in raw]) ** 0.5
        return [x / float(length) for x in raw]


class System:
    def __init__(self):
        self.particles = list()
        self.forces = list()
        self.emitters = list()

    def simulate(self, time_step=1.0):
        for p in self.particles:
            # position
            for f in self.forces:
                for i in range(2):
                    a = f[i] / p.mass
                    p.velocity[i] += a * time_step
                    p.position[i] += p.velocity[i] * time_step
            # collision
            if p.position[1] < 0.0:  # ground
                p.position[1] = 0.0
                p.velocity[1] *= -0.75
        # emit
        for e in self.emitters:
            for p in e.emit():
                self.particles.append(p)
