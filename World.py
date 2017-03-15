"""World.py world object """
__author__ = "Jesse Lessard"
__copyright__ = "Copyright 2017, Jesse Lessard"
__license__ = "GPLv3"
__maintainer__ = "Jesse Lessard"
__email__ = "jhlessard@live.com"
__status__ = "Development"

import numpy

class World:

    def __init__(self):
        self.gravity = 9.8          #(m/s^2)
        self.airdensity = 1

    def force_on(self, rocket):
        # force from gravity
        f = numpy.array([0,0,-rocket.mass*self.gravity])

        # force from air - drag

        return f
