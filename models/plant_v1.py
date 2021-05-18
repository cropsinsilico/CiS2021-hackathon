import os
import trimesh
import argparse
import numpy as np
from yggdrasil import units
from yggdrasil.languages.Python.YggInterface import YggRpcClient, YggOutput

_dir = os.path.dirname(os.path.realpath(__file__))

def run(mesh, tmin, tmax, tstep):
    mass = 2000.0
    light_rpc = YggRpcClient('light_plant')
    light_out = YggOutput('light')
    mass = units.add_units(mass, 'g')
    tmin = units.add_units(tmin, 'hrs')
    tmax = units.add_units(tmax, 'hrs')
    tstep = units.add_units(tstep, 'hrs')
    t = tmin
    i = 0

    while t <= tmax:

        # Get light data by calling light model
        flag, light = light_rpc.call(mesh.vertices[:, 2], t)
        if not flag:
            raise Exception("Error calling light model")
        
        # Grow mesh
        # (pretend this is a biologically complex calculation)
        scale = units.get_data(mass * light / units.add_units(1.0, 'kg'))
        mesh.vertices[:, 2] += mesh.vertices[:, 2] * scale

        # Save mesh for this timestep
        filename_mesh = os.path.join(_dir, f'../output/mesh_{i:03d}.obj')
        with open(filename_mesh, 'w') as fd:
            mesh.export(fd, 'obj')

        # Send light to output
        flag = light_out.send(light)
        if not flag:
            raise Exception("Error sending light to output")

        # Advance time step
        t += tstep
        i += 1

    return mesh


# Parse command-line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser("Simulate plant growth over time.")
    parser.add_argument('tmin', help='Starting time (in hours)', type=float)
    parser.add_argument('tmax', help='Ending time (in hours)', type=float)
    parser.add_argument('tstep', help='Time step (in hours)', type=float)
    parser.add_argument('--meshfile', help='Path to file where mesh is stored.',
                        default='../meshes/plants-2.obj')
    args = parser.parse_args()
    mesh = trimesh.load_mesh(args.meshfile)
    run(mesh, args.tmin, args.tmax, args.tstep)
