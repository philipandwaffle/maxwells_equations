import numpy as np

class VecField:
    def __init__(self, shape):
        self.field = np.zeros((shape[0],shape[0],2))
