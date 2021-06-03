import os
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
    
    # Check if model is running as a part of an yggdrasil integration
    with_yggdrasil = os.environ.get('YGG_SUBPROCESS', False)

    # If the model is running as part of an yggdrasil integration, import
    # the relevant yggdrasil routines and use the interface routine to
    # complete the connection defined in the YAML
    if with_yggdrasil:
        from yggdrasil.languages.Python.YggInterface import YggRpcClient
        weather_rpc = YggRpcClient('weather_light', global_scope=True)

        # Call the weather model
        flag, temp = weather_rpc.call(intensity)
        if not flag:
            raise Exception("Failed to call the weather model.")

        # Return both the intensity and temp
        return intensity, temp


    return intensity
