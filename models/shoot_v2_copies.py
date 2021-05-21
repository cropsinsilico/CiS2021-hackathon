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
    import numpy as np
    import pickle
    from yggdrasil import units
    from yggdrasil.languages.Python.YggInterface import YggRpcClient
    light_rpc = YggRpcClient('light_shoot')

# Continue simulation until time limit is reached
while t <= tmax:

    # If running as part an yggdrasil integration, send the time and
    # maximum height of the mesh to the height channel with units
    if with_yggdrasil:
        # Send requests to the light model for each mesh vertex
        for v in mesh.vertices[:, 2]:
            flag = light_rpc.send(
                [units.add_units(t, 'hrs'),
                 units.add_units(v, 'm')])
            if not flag:
                raise Exception("Error sending request to the light model.")

        # Calculations that don't rely on the output from the light model
        # can be run here in parallel with the light model calculations

        # Receive responses from the light model for each mesh vertex
        nvert = mesh.vertices.shape[0]
        intensity = np.zeros(nvert, 'f8')
        for iv in range(nvert):
            flag, v_intensity = light_rpc.recv()
            if not flag:
                raise Exception("Error receiving response from the light model.")
            if not units.has_units(intensity):
                intensity = units.add_units(intensity,
                                            units.get_units(v_intensity))
            intensity[iv] = v_intensity
        filename_light = os.path.join(_dir, f'../output/light_{i:03d}.pkl')
        with open(filename_light, 'wb') as fd:
            pickle.dump(intensity, fd)

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
