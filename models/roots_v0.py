import os
import argparse
import pickle

_dir = os.path.dirname(os.path.realpath(__file__))

# Parse command-line arguments
parser = argparse.ArgumentParser("Simulate root growth over time.")
parser.add_argument('tmin', help='Starting time (in days)', type=float)
parser.add_argument('tmax', help='Ending time (in days)', type=float)
parser.add_argument('tstep', help='Time step (in days)', type=float)
args = parser.parse_args()
tmin = args.tmin
tmax = args.tmax
tstep = args.tstep

# Set initial conditions
mass = 0.0
t = tmin
times = []
masses = []

# Continue simulation until time limit is reached
while t <= tmax:

    # Compute the scale factor
    # (pretend this is a biologically complex calculation)
    scale = 0.2
    
    # Calculate mass for the time step
    # (pretend this is a biologically complex calculation)
    mass += t * scale

    # Add mass & time to array
    times.append(t)
    masses.append(mass)

    # Advance time step
    t += tstep

# Write the total mass array to output
filename_masses = os.path.join(_dir, '../output/masses.pkl')
with open(filename_masses, 'wb') as fd:
    pickle.dump({'times': times, 'masses': masses}, fd)
