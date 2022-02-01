from config import WIDTH, HEIGHT


class Effect:
    def __init__(self):
        self.particles = []

    def append(self, particles_array):
        self.particles += particles_array
        for particle in self.particles:
            self.particles += [particle.trace()] if particle.trace_shrink_speed else []

    def remove_particle(self, particle):
        if any([particle.radius < 0,
                particle.x < -particle.radius, particle.x > WIDTH + particle.radius,
                particle.y < -particle.radius, particle.y > HEIGHT + particle.radius]):
            self.particles.remove(particle)

    def draw(self, screen):
        for particle in self.particles:
            self.particles += [particle.trace()] if particle.trace_shrink_speed else []
            self.remove_particle(particle)
            particle.draw(screen)
