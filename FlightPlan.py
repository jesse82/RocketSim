#!/usr/local/bin/python
# -*- coding: iso-8859-15 -*-

"""FlightPlan.py what we want our rocket to do"""
__author__ = "Jesse Lessard"
__copyright__ = "Copyright 2017, Jesse Lessard"
__license__ = "GPLv3"
__maintainer__ = "Jesse Lessard"
__email__ = "jhlessard@live.com"
__status__ = "Development"

# The flight plann is more of script so we wont bother with an object
# the rocket will check its flight plan at a given t (time) and set its relavent properties
from Rocket import Rocket

def FlightPlan(t, rocket):
    if t < 0:
        rocket.power = 0
    elif t < 120:
        rocket.power = 100
    elif t < 200:
        rocket.power = 75
    elif t < 500:
        rocket.power = 10
