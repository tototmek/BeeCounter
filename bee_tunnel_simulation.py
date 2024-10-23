import sys
import core
import display

display = display.Display((800, 600))


class Simulation:
    bees: list
    sensors: list
    dt: float
    time: float
    bee_count: int


sim = Simulation()
sim.bees = [core.Bee(0, 0.1, 0.1)]
sim.sensors = [core.Sensor(0.25, 0.1), core.Sensor(0.75, 0.1)]
sim.dt = 0.017
sim.bee_count = 0
sim.time = 0.0

spawner = core.Spawner(
    [
        core.SpawnEvent(3.0, -0.5, 0.05, 0.12),
        core.SpawnEvent(5.0, 1.5, 0.05, -0.12),
        core.SpawnEvent(7.0, -0.5, 0.05, 0.12),
        core.SpawnEvent(8.0, 1.5, 0.05, -0.12),
    ]
)

try:
    while True:
        for bee in sim.bees:
            bee.step(sim.dt)
            if bee.position < -0.5 or bee.position > 1.5:
                sim.bees.remove(bee)
        for sensor in sim.sensors:
            sensor.reset()
            for bee in sim.bees:
                sensor.detect(bee)
        sim.time += sim.dt
        spawner.step(sim)
        display.update(sim)
except KeyboardInterrupt:
    sys.exit()
