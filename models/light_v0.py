import numpy as np
from yggdrasil import units


def light(doy, height):
    r"""Compute the intensity of light.

    Args:
       doy (float): Day of year.
       height (float): Distance from ground in cm.

    Returns:
       float: Intensity of light in ergs cm^-2 s^-1.

    """
    # Define parameters that are static across a run
    amplitude = units.add_units(80.0, 'ergs cm^-3 s^-1')
    doy_offset = units.add_units(0.0, 'days')

    # Calculate intensity
    intensity = (
        amplitude * height *
        (1.0 + np.sin(2.0 * np.pi * (doy - doy_offset) /
                      units.add_units(365.0, 'days'))))
    
    return intensity
