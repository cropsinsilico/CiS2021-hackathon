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

# Check if model is running as a part of an yggdrasil integration
with_yggdrasil = os.environ.get('YGG_SUBPROCESS', False)

# If the model is running as part of an yggdrasil integration, import
# the relevant yggdrasil routines and use the interface routine to
# complete the connection defined in the YAML
if with_yggdrasil:
    from yggdrasil import units
    from yggdrasil.languages.Python.YggInterface import YggRpcClient
    light_rpc = YggRpcClient('light_shoot')

# Continue simulation until time limit is reached
while t <= tmax:

    # If running as part an yggdrasil integration, send the time and
    # maximum height of the mesh to the height channel with units
    if with_yggdrasil:
        flag, intensity = light_rpc.call(
            [units.add_units(t, 'hrs'),
             units.add_units(max(mesh.vertices[:, 2]), 'm')])
        if not flag:
            raise Exception("Error calling the light model.")

        # Compute the scale factor using intensity, stripping units
        # of the result to allow use with trimesh
        # (pretend this is a biologically complex calculation)
        scale = units.get_data(
            units.add_units(mass, 'g') * intensity /
            units.add_units(4.0e10, 'g*erg/(cm**2*s)'))
        
    else:
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
