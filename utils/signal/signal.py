from typing import Union

import numpy as np
import matplotlib.pyplot as plt


class Signal:
    def __init__(self,
                 frequency: Union[float, int],
                 amplitude: Union[float, int],
                 bias: Union[float, int],
                 duration: Union[float, int],
                 sampling_rate: float = 0.01):
        self.frequency = frequency
        self.amplitude = amplitude
        self.bias = bias
        self.duration = duration
        self.sampling_rate = sampling_rate

        self.x = np.linspace(0, self.duration * np.pi, int(self.duration / self.sampling_rate))

    @property
    def sine(self) -> np.ndarray:
        return self.amplitude * np.sin(self.frequency * self.x) + self.bias

    def plot(self) -> None:
        plt.plot(self.x, self.sine)
        plt.show()
