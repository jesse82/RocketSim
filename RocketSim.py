#!/usr/local/bin/python
# -*- coding: iso-8859-15 -*-

"""RocketSim.py: RocketSim main run file"""

__author__ = "Jesse Lessard"
__copyright__ = "Copyright 2017, Jesse Lessard"
__license__ = "GPLv3"
__maintainer__ = "Jesse Lessard"
__email__ = "jhlessard@live.com"
__status__ = "Development"

import numpy
from matplotlib.pyplot import * # Grab MATLAB plotting functions
from Rocket import *
from World import *
from FlightPlan import *

#main simulation loop

runtime = 500           # runtime in (s)
deltaT = 1
rocket = Rocket()
world = World()


time = 0

#variables for plots
times = []
accelerations = []
velocities = []
positions = []
accelerations = []

while time <= runtime:
    time += deltaT

    #update rocket params with the flight plan
    FlightPlan(time, rocket)
    # F = ma, get applied forces and calculate curren time step aceleration
    # then use deltaT to update rocks speed/position at the end of this time step
    a = rocket.force()/rocket.mass + world.force_on(rocket)/rocket.mass
    # velocity = acceleration*time => dv = a.dt
    dv = a*deltaT

    #update rockt
    rocket.position += deltaT*(rocket.volocity + rocket.volocity + dv)/2
    rocket.volocity += dv
    rocket.fuel -= (rocket.power/100)*rocket.consumption*deltaT

    # keep data from plots
    times.append(time)
    accelerations.append(a[2])
    velocities.append(rocket.volocity[2])
    positions.append(rocket.position[2])


subplot(311)
title("Position")
plot(times, positions)
subplot(312)
title("Velocity")
plot(times, velocities)
subplot(313)
title("Acceleration")
plot(times, accelerations)

show()

print(positions[0])
print(positions[100])

# arcarrow([1.3, 0.8], [5, 0.45], -6);
