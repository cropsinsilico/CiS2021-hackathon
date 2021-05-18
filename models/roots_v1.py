import os
import argparse
from yggdrasil import units
from yggdrasil.languages.Python.YggInterface import YggOutput, YggTimesync


def run(tmin, tmax, tstep):
    mass_out = YggOutput('mass')
    plant2root = YggTimesync('plant2root')
    tmin = units.add_units(tmin, 'days')
    tmax = units.add_units(tmax, 'days')
    tstep = units.add_units(tstep, 'days')
    t = tmin
    mass = 0

    while t <= tmax:

        # Calculate mass for the time step
        # (pretend this is a biologically complex calculation)
        mass += t * units.add_units(0.2, 'kg/days')

        # Synchronize data for time step with the root model
        plant_state = {'mass': mass}
        flag, plant_state = plant2root.call(t, plant_state)
        if not flag:
            raise Exception("Error performing time-step synchronization "
                            "with plant model.")
    
        # Send masses to output
        flag = mass_out.send({'time': t,
                              'total_mass': plant_state['mass'],
                              'root_mass': mass,
                              'plant_mass': plant_state['mass'] - mass})
        if not flag:
            raise Exception("Error sending masses to output")

        # Advance time step
        t += tstep

    return mass


# Parse command-line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser("Simulate root growth over time.")
    parser.add_argument('tmin', help='Starting time (in days)', type=float)
    parser.add_argument('tmax', help='Ending time (in days)', type=float)
    parser.add_argument('tstep', help='Time step (in days)', type=float)
    args = parser.parse_args()
    run(args.tmin, args.tmax, args.tstep)
