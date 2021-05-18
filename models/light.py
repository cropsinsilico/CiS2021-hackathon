import numpy as np
from yggdrasil import units


def light(height, time):
    intensity = (
        80.0 *
        (1.0 + np.sin(2.0 * np.pi * time / units.add_units(365.0, 'days'))) /
        (np.abs(200 - height)**2))
    return intensity
