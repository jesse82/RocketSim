"""Rocket.py rocket object with conrol system"""
__author__ = "Jesse Lessard"
__copyright__ = "Copyright 2017, Jesse Lessard"
__license__ = "GPLv3"
__maintainer__ = "Jesse Lessard"
__email__ = "jhlessard@live.com"
__status__ = "Development"

import numpy

class Rocket:

    def __init__(self):
        self.Cg = numpy.array([0,0,1000],float)        # center of gravity (mm)
        self.orentation = numpy.array([0,0,1], float)  # z being upright
        self.position = numpy.array([0,0,0], float)
        self.volocity = numpy.array([0,0,0], float)

        self.power = 0                              # 0 being off, 100 full
        self.mass = 1000                            # mass of rocket (kg)
        self.fuel = 100                             # mass of fuel (kg)
        self.consumption = 1                        # fuel consumed at full power (kg/min)
        self.maxthrust = 10000                      # max power thrust (n)


    def force(self):
        # force from the rockets moter
        # TODO project force into orentation
        f = numpy.array([0,0,(self.power/100)*self.maxthrust], float)

        return f
