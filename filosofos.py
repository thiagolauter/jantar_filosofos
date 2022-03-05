import random
import time
import logging

from threading import Thread


format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")


class Filosofo(Thread):
    id: int
    direito: int
    esquerdo: int
    mesa: object

    def __init__(self, id, mesa):
        Thread.__init__(self)
        self.id = id
        self.mesa = mesa
        self.direito = id - 1
        if (id == len(self.mesa.garfos)):
            self.esquerdo = 0
        else:
            self.esquerdo = id

    def run(self):
        while 1 > 0:
            self.comer()
            self.pensar()


    def comer(self):
        self.mesa.lock.acquire()
        if (self.mesa.garfos[self.direito] < 0) and (self.mesa.garfos[self.esquerdo] < 0):
            print(self.id, 'comer')
            self.mesa.garfos[self.direito] = self.id
            self.mesa.garfos[self.esquerdo] = self.id
            print(self.mesa.garfos)
            self.mesa.lock.release()
            time.sleep(random.uniform(2, 3))
            return 0
        else:
            self.mesa.lock.release()
        return 1

    def pensar(self):
        self.mesa.lock.acquire()
        if (self.mesa.garfos[self.direito] == self.id) & (self.mesa.garfos[self.esquerdo] == self.id):
            print(self.id, 'pensar')
            self.mesa.garfos[self.direito] = -1
            self.mesa.garfos[self.esquerdo] = -1
            print(self.mesa.garfos)
            self.mesa.lock.release()
            time.sleep(random.uniform(0.3, 2))
            return 0
        else:
            self.mesa.lock.release()
        return 1
