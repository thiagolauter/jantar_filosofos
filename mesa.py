from threading import Lock

class Mesa():
    garfos: list
    lock = object

    def __init__(self, num_garfos):
        self.garfos = [-1] * num_garfos
        self.lock = Lock()
        pass