import random
import time

from pymobiledevice3.services.dvt.instruments.location_simulation import LocationSimulation

from utils import bd09Towgs84, fixLockT, randLoc

def simulat_run(dvt, loc, random_v, dt=0.2):
    fixedLoc = fixLockT(loc, random_v, dt)
    nList = (5, 6, 7, 8, 9)
    n = nList[random.randint(0, len(nList)-1)]
    fixedLoc = randLoc(fixedLoc, n=n)  # a path will be divided into n parts for random route
    clock = time.time()
    for i in fixedLoc:
        LocationSimulation(dvt).set(*bd09Towgs84(i).values())
        while time.time()-clock < dt:
            pass
        clock = time.time()