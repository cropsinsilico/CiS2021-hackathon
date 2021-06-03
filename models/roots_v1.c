#include <stdio.h>
#include <stdlib.h>
// Only include yggdrasil header if compiled with the WITH_YGGDRASIL definition
#ifdef WITH_YGGDRASIL
#include "YggInterface.h"
#endif // WITH_YGGDRASIL


int main(int argc, char *argv[]) {
  int i, flag, nstep;
  float tmin, tmax, tstep, mass, t, scale;
  float* times;
  float* masses;

  // Parse command-line arguments
  if (argc!=4) {
    printf("tmin, tmax, and tstep must be specified.\n");
    return -1;
  }
  tmin = atof(argv[1]);
  tmax = atof(argv[2]);
  tstep = atof(argv[3]);

  // Set initial conditions
  i = 0;
  mass = 0.0;
  t = tmin;
  nstep = (int)(ceil((tmax - tmin) / tstep));
  times = (float*)malloc(nstep * sizeof(float));
  masses = (float*)malloc(nstep * sizeof(float));

#ifdef WITH_YGGDRASIL
  // If the model is running as part of an yggdrasil integration,
  // use yggdrasil interface routines to complete the connection
  // defined in the YAML
  comm_t* shoot2root = yggTimesync("shoot2root", "days");
#endif // WITH_YGGDRASIL

  // Continue simulation until time limit is reached
  while (t < (tmax + 0.0001)) {

#ifdef WITH_YGGDRASIL
    // If running as part an yggdrasil integration, send the time and
    // mass to the timesync channel and then updated the mass based on
    // the returned state
    generic_t root_state = init_generic_map();
    generic_t total_state = init_generic_map();
    flag = generic_map_set_double(root_state, "mass", mass, "kg");
    if (flag < 0) {
      printf("ERROR: failed to initialize state.");
      return -1;
    }
    flag = rpcCall(shoot2root, t, root_state, &total_state);
    if (flag < 0) {
      printf("ERROR: Error performing time-step synchronization with shoot model.");
      return -1;
    }
    
    // Compute the scale factor using total mass
    // (pretend this is a biologically complex calculation)
    scale = 0.05 * generic_map_get_double(total_state, "mass");

    // Cleanup state
    destroy_generic(&root_state);
    destroy_generic(&total_state);
#else
    // Compute the scale factor
    // (pretend this is a biologically complex calculation)
    scale = 0.2;
    
#endif // WITH_YGGDRASIL
    
    // Calculate mass for the time step
    // (pretend this is a biologically complex calculation)
    mass = mass + t * scale;
    
    // Add mass & time to array
    times[i] = t;
    masses[i] = mass;

    // Advance time step
    t = t + tstep;
    i++;
  
  }

  // Write the total mass array to output
  FILE *fd = fopen("../output/masses.txt", "w");
  if (fd == NULL) {
    printf("ERROR: Failed to open output file.\n");
    fclose(fd);
    return -1;
  }
  for (i = 0; i < nstep; i++) {
    if (fprintf(fd, "%f\t%f\n", times[i], masses[i]) < 0) {
      printf("ERROR: Failed to write masses to output.\n");
      fclose(fd);
      return -1;
    }
  }

  // Free variables
  free(times);
  free(masses);
  return 0;
}
