import os
import trimesh
import argparse

_dir = os.path.dirname(os.path.realpath(__file__))

# Parse command-line arguments
parser = argparse.ArgumentParser("Simulate a shoot's growth over time.")
parser.add_argument('tmin', help='Starting time (in hours)', type=float)
parser.add_argument('tmax', help='Ending time (in hours)', type=float)
parser.add_argument('tstep', help='Time step (in hours)', type=float)
parser.add_argument('--meshfile', help='Path to file where mesh is stored.',
                    default='../meshes/plants-2.obj')
args = parser.parse_args()
tmin = args.tmin
tmax = args.tmax
tstep = args.tstep
mesh = trimesh.load_mesh(args.meshfile)

# Set initial conditions
mass = 2000.0
t = tmin
i = 0

# Continue simulation until time limit is reached
while t <= tmax:

    # Compute the scale factor
    # (pretend this is a biologically complex calculation)
    scale = mass / 4.5e4

    # Grow the shoot
    # (pretend this is a biologically complex calculation)
    mesh.vertices[:, 2] += mesh.vertices[:, 2] * scale
    mass += mass * scale

    # Save mesh for this timestep
    filename_mesh = os.path.join(_dir, f'../output/mesh_{i:03d}.obj')
    with open(filename_mesh, 'w') as fd:
        mesh.export(fd, 'obj')

    # Advance time step
    t += tstep
    i += 1
