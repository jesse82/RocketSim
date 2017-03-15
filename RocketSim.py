#!/usr/bin/env python2.7

"""RocketSim.py: RocketSim main run file"""

__author__ = "Jesse Lessard"
__copyright__ = "Copyright 2017, Jesse Lessard"
__license__ = "GPLv3"
__maintainer__ = "Jesse Lessard"
__email__ = "jhlessard@live.com"
__status__ = "Development"

import numpy
from Rocket import *
from World import *
from FlightPlan import *

#main simulation loop

runtime = 500           # runtime in (s)
deltaT = 0.1
rocket = Rocket()
world = World()


time = -1

while time <= runtime:
    time += deltaT

    #update rocket params with the flgitplan
    FlightPlan(time, rocket)
    # F = ma, get applied forces and calculate curren time step aceleration
    # then use detlaT to update rocks speed/position at the end of this time step
    a = rocket.force()/rocket.mass + world.force_on(rocket)/rocket.mass
    # velocity = acceleration*time => dv = a.dt
    dv = a*deltaT
    rocket.position += deltaT*(rocket.volocity + rocket.volocity + dv)/2
    rocket.volocity += dv
    rocket.fuel -= (rocket.power/100)*rocket.consumption*detlaT

print rocket.position
print rocket.volocity
