import logging
import time

from filosofos import Filosofo
from mesa import Mesa


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    mesa = Mesa(5)
    print(mesa)
    print('S')
    f = []
    print(mesa.garfos)
    for i in range(5):
        f.append(Filosofo(i, mesa))
        f[i].start()
    print('End')
