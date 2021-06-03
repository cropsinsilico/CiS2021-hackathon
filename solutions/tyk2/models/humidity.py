import numpy as np
from yggdrasil import units
from yggdrasil.languages.Python.YggInterface import YggInput, YggOutput


def calc(doy, height, co2):
    return 3.0e8 * np.cos(2.0 * np.pi * doy / units.add_units(365, 'days')) / (co2 * height**3)


# Create input and output comms
height_in = YggInput('height')
conc_in = YggInput('co2')
humidity_out = YggOutput('humidity')

# Keep looping until there are no more inputs
while True:

    # Receive height
    flag, height_data = height_in.recv()
    if not flag:
        print("No more inputs")
        break
    [doy_height, height] = height_data[:]

    # Receive co2
    flag, [doy_co2, co2] = conc_in.recv()
    if not flag:
        raise Exception("Error receiving co2 input")

    # Check that height and co2 days match
    assert(doy_height == doy_co2)
    doy = doy_height

    # Call calculation
    humidity = calc(doy, height, co2)
    print('Humidity', doy, height, co2, humidity)

    # Send humidity
    flag = humidity_out.send(doy, height, co2, humidity)
    if not flag:
        raise Exception("Error sending humidity to output")
