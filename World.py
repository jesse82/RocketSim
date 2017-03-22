#!/usr/local/bin/python
# -*- coding: iso-8859-15 -*-

"""World.py world object """
__author__ = "Jesse Lessard"
__copyright__ = "Copyright 2017, Jesse Lessard"
__license__ = "GPLv3"
__maintainer__ = "Jesse Lessard"
__email__ = "jhlessard@live.com"
__status__ = "Development"

import numpy
import math

class World:

    def __init__(self):
        self.gravity = 9.8          #(m/s^2)
        self.G = 6.67408E-11
        self.mass_earth = 5.972E24
        self.d0 = 6371e3

        self.rho0 = 1.225 # (Kg/m3)
        self.T0 = 288.16 # (K)
        self.a = 0.0065 # (K/m)
        self.n = 5.2561

        self.c1 = 1.1  # coef for air pressure forces (friction coef)

    def force_on(self, rocket):
        # force from gravity: F = G (m1*m2/d^2)
        # G = 6.67408 × 10-11 m3 kg-1 s-2
        # m1 = mass earth = 5.972 × 10^24 kg
        # radius earth = 6371km
        f = numpy.array([0,0,- self.G*(rocket.mass*self.mass_earth/math.pow(self.d0 + rocket.position[2], 2))])
        # this force is applied at the rockets center of gravity


        #density of air..
        #ρ(h) / ρ0 = ( T(h) / T0 )^(n−1)
        # T(h) = T0 -ah
        Th = self.T0 - self.a*rocket.position[2]

        # once temp is about 0 then desnity is also near 0 -> we can neglect this force
        if Th > 0:
            rho = self.rho0*numpy.power((Th/self.T0),(self.n - 1))
            #force air pressure = .5 rho S V^2 c1
            # force from air - drag
            fp = .5*rho*math.pow(rocket.volocity[2], 2)*self.c1

            signV = numpy.sign(rocket.volocity[2])
            f += numpy.array([0,0, -signV*fp])

        return f
