import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib
matplotlib.use('TkAgg')


# Setup a Vec3D class.
class Vec3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vec3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, scalar):
        return Vec3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar):
        return Vec3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __sub__(self, other):
        return Vec3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __truediv__(self, scalar):
        return Vec3D(self.x / scalar, self.y / scalar, self.z / scalar)

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
        self.G = 0.5

        self.i = Particle.n
        Particle.n += 1

    def calculate_acceleration(self, particles):
        self.acceleration = Vec3D(0, 0, 0)
        for j in range(len(particles)):
            if self.i != j:
                dir_vec = particles[j].position - self.position
                len_vec = dir_vec.get_length()
                unit_vec = dir_vec * 1 / len_vec
                if len_vec == 0:
                    continue
                f = (self.G * self.mass * particles[j].mass) / len_vec ** 2
                self.acceleration += (f / self.mass) * unit_vec

    def update(self, dt):
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt

par = []

############### Setting up the simulation ###############
par.append(Particle(Vec3D(0, 0, 0), Vec3D(0.5, 0.5, 0.5), 1))
par.append(Particle(Vec3D(0, 0, 10), Vec3D(0.5, 0.5, 0.5), 1))
par.append(Particle(Vec3D(-10, 10, 0), Vec3D(0.5, 0.5, 2), 100))
dt = 1

#########################################################


n = len(par)
# Plotting the simulation
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Initialize initial positions
positions = np.array([[p.position.x, p.position.y, p.position.z] for p in par])
scat = ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2])

ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.set_zlim(-100, 100)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


def init():
    return scat,


def update(frame):
    for i in range(n):
        par[i].calculate_acceleration(par)
        par[i].update(dt)

    positions = np.array([[p.position.x, p.position.y, p.position.z] for p in par])
    scat._offsets3d = (positions[:, 0], positions[:, 1], positions[:, 2])
    return scat,


ani = FuncAnimation(fig, update, init_func=init, frames=100, interval=50, blit=False)

plt.show()
