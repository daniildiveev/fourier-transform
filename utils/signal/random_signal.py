import numpy as np

from .signal import Signal


class RandomSignal(Signal):
    def __init__(self):
        super().__init__(np.random.random(1) * np.random.randint(1, 100),
                         np.random.random(1) * np.random.randint(1, 100),
                         np.random.random(1) * np.random.randint(1, 100),
                         np.random.random(1) * np.random.randint(1, 100),
                         np.random.random(1))
