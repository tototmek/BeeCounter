class Bee:
    def __init__(self, position, radius, speed) -> None:
        self.position = position
        self.radius = radius
        self.speed = speed

    def step(self, dt) -> None:
        self.position += self.speed * dt


class Sensor:
    def __init__(self, position, radius) -> None:
        self.position = position
        self.radius = radius
        self.triggered = False

    def detect(self, bee: Bee) -> None:
        detection = (bee.position - bee.radius < self.position + self.radius) and (
            self.position - self.radius < bee.position + bee.radius
        )
        self.triggered = self.triggered or detection

    def reset(self) -> None:
        self.triggered = False


class SpawnEvent:
    def __init__(self, time, bee_position, bee_radius, bee_speed):
        self.time = time
        self.bee_position = bee_position
        self.bee_radius = bee_radius
        self.bee_speed = bee_speed


class Spawner:
    def __init__(self, sequence: list) -> None:
        self.sequence = sequence

    def step(self, simulation):
        if not len(self.sequence):
            return
        event: SpawnEvent = self.sequence[0]
        if simulation.time > event.time:
            simulation.bees.append(
                Bee(event.bee_position, event.bee_radius, event.bee_speed)
            )
            self.sequence.pop(0)
