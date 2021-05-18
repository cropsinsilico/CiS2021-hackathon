import os
import argparse


def run(tmin, tmax, tstep):
    t = tmin
    mass = 0

    while t <= tmax:

        # Calculate mass for the time step
        # (pretend this is a biologically complex calculation)
        mass += t * 0.2

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
