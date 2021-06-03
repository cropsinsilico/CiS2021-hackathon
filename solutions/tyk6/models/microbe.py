import os
import argparse
import pickle

_dir = os.path.dirname(os.path.realpath(__file__))

# Parse command-line arguments
parser = argparse.ArgumentParser("Simulate microbe growth over time.")
parser.add_argument('tmin', help='Starting time (in min)', type=float)
parser.add_argument('tmax', help='Ending time (in min)', type=float)
parser.add_argument('tstep', help='Time step (in min)', type=float)
args = parser.parse_args()
tmin = args.tmin
tmax = args.tmax
tstep = args.tstep

# Set initial conditions
mass = 0.1
t = tmin
times = []
masses = []

# Check if model is running as a part of an yggdrasil integration
with_yggdrasil = os.environ.get('YGG_SUBPROCESS', False)

# If the model is running as part of an yggdrasil integration, import
# the relevant yggdrasil routines and use the interface routine to
# complete the connection defined in the YAML
if with_yggdrasil:
    from yggdrasil import units
    from yggdrasil.languages.Python.YggInterface import YggTimesync
    shoot2microbe = YggTimesync('shoot2root')
    
# Continue simulation until time limit is reached
while t <= tmax:

    # If running as part an yggdrasil integration, send the time and
    # mass to the timesync channel and then updated the mass based on
    # the returned state
    if with_yggdrasil:
        microbe_state = {'mass': units.add_units(mass, 'g')}
        flag, total_state = shoot2microbe.call(units.add_units(t, 'days'),
                                               microbe_state)
        if not flag:
            raise Exception("Error performing time-step synchronization "
                            "with shoot model.")
        
        # Compute the scale factor using total mass, stripping units
        # of the result to allow use with original code
        # (pretend this is a biologically complex calculation)
        scale = units.get_data(
            units.convert_to(
                units.add_units(0.005, 'min-1') * total_state['mass'],
                'g/min'))

    else:
        # Compute the scale factor
        # (pretend this is a biologically complex calculation)
        scale = 0.0007
    
    # Calculate mass for the time step
    # (pretend this is a biologically complex calculation)
    mass += t * scale

    # Add mass & time to array
    times.append(t)
    masses.append(mass)

    # Advance time step
    t += tstep

# Write the total mass array to output
filename_masses = os.path.join(_dir, '../output/microbe_masses.pkl')
with open(filename_masses, 'wb') as fd:
    pickle.dump({'times': times, 'masses': masses}, fd)
