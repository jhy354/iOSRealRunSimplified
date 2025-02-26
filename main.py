import random
import asyncio

from pymobiledevice3.remote.remote_service_discovery import RemoteServiceDiscoveryService
from pymobiledevice3.services.os_trace import OsTraceService
from pymobiledevice3.remote.remote_service_discovery import RemoteServiceDiscoveryService
from pymobiledevice3.services.dvt.instruments.location_simulation import LocationSimulation
from pymobiledevice3.services.dvt.dvt_secure_socket_proxy import DvtSecureSocketProxyService

from utils import get_route
from core import simulat_run

async def main(full_address: tuple,loc: list):
    rsd = RemoteServiceDiscoveryService(full_address)
    await rsd.connect()
    dvt = DvtSecureSocketProxyService(rsd)
    dvt.perform_handshake()

    while True:
        random_v = 1000/(1000/3-(2*random.random()-1)*15)
        simulat_run(dvt, loc, random_v)
        print("Lap Finished!")

if __name__ == "__main__":

    host = str(input("HOST:"))
    port = int(input("PORT:"))
    full_address = (host, port)
    
    asyncio.run(main(full_address, get_route()))
