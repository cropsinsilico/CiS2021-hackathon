import argparse
import numpy as np
import os

def calculate_concentration(doy, dist, height, offset=60.0):
    r"""Function that calculates the concentration of CO2.

    Args:
        doy (float): Day of year.
        dist (float): Distance from the plant in cm.
        height (float): Distance from the ground in cm.
        offset (float, optional): Offset in the year in days. Defaults to 60.

    Returns:
        float: CO2 concentration in cm^-3

    """
    return np.sin(2.0 * np.pi * (doy + offset) / 365) / (dist * dist * height)


# Parse command-line arguments
parser = argparse.ArgumentParser("Calculate the co2 concentration at a given distance from a plant.")
parser.add_argument('dist', help='Distance from the plant (cm)', type=float)
parser.add_argument('height', help='Distance from the ground (cm)', type=float)
parser.add_argument('doy', help='Day of year', type=float)
args = parser.parse_args()
dist = args.dist
height = args.height
doy = args.doy
offset = 60.0

# Check if model is running as a part of an yggdrasil integration
with_yggdrasil = os.environ.get('YGG_SUBPROCESS', False)

# If the model is running as part of an yggdrasil integration, import
# the relevant yggdrasil routines and use the interface routine to
# complete the connection defined in the YAML
if with_yggdrasil:
    from yggdrasil import units
    from yggdrasil.languages.Python.YggInterface import YggInput, YggOutput
    height_in = YggInput('height')
    conc_out = YggOutput('co2')

    # Add units to parameters
    dist = units.add_units(dist, 'cm')
    offset = units.add_units(offset, 'days')

    # Loop over input
    while True:
        # Receive height
        flag, height_data = height_in.recv()
        if not flag:
            print('End of height input')
            break
        [doy, height] = height_data[:]

        
        # Compute concentration
        conc = calculate_concentration(doy, dist, height, offset=offset)
        print('Concentration', conc)

        # Send output
        flag = conc_out.send(doy, conc)
        if not flag:
            raise Exception("Error sending concentration to output")

else:
    
    # Compute concentration
    conc = calculate_concentration(doy, dist, height)
    print('Concentration', conc)
