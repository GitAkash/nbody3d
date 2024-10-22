import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Setup a Vec3D class.
class Vec3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_length(self):
        return np.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

# Setting up particles.
class Particle:
    n = 0

    def __init__(self, position, velocity, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.acceleration = Vec3D(0, 0, 0)
        self.G = 1

        self.i = Particle.n
        Particle.n += 1

    def calculate_acceleration(self, particles):
        self.acceleration = Vec3D(0, 0, 0)
        for j in range(len(particles)):
            if self.i != j:
                dir_vec = self.position - particles[j].position
                len_vec = dir_vec.get_length()
                unit_vec = dir_vec / len_vec
                if len_vec == 0:
                    continue
                f = (self.G * self.mass * particles[j].mass) / len_vec ** 2
                self.acceleration += (f / self.mass) * unit_vec

    def update(self, dt):
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt


# Setting up the simulation
par = []
par.append(Particle(Vec3D(0, 0, 0), Vec3D(0.5, 0.5, 0.5), 1))




