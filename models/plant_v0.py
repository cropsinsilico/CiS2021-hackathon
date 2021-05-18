import os
import trimesh
import argparse

_dir = os.path.dirname(os.path.realpath(__file__))

def run(mesh, tmin, tmax, tstep):
    mass = 2000.0
    t = tmin
    i = 0

    while t <= tmax:

        # Grow mesh
        # (pretend this is a biologically complex calculation)
        scale = mass * t / 3.5e5
        mesh.vertices[:, 2] += mesh.vertices[:, 2] * scale

        # Save mesh for this timestep
        filename_mesh = os.path.join(_dir, f'../output/mesh_{i:03d}.obj')
        with open(filename_mesh, 'w') as fd:
            mesh.export(fd, 'obj')

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
