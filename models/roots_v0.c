#include <stdio.h>
#include <stdlib.h>


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

  // Continue simulation until time limit is reached
  while (t < (tmax + 0.0001)) {

    // Compute the scale factor
    // (pretend this is a biologically complex calculation)
    scale = 0.2;
    
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
