import numpy as np
from yggdrasil import units


def temp(intensity):
    r"""Compute the temperature based on the intensity of light.

    Args:
        intensity (float): Intensity of light in ergs cm^-2 s^-1.

    """
    if not units.has_units(intensity):
        intensity = units.add_units(intensity, 'erg/(cm**2*s)')
    sigma = units.add_units(5.67e-8, 'W m^-2 K^-4')
    T = (np.pi * intensity / sigma)**0.25
    T.convert_to_cgs()
    return T
