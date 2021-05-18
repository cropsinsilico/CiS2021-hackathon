#define _USE_MATH_DEFINES  // Required to use M_PI with MSVC
#include <math.h>

int light(double* height, uint64_t length_height, double time,
	  double** intensity, uint64_t* length_intensity) {
  (*intensity) = (double*)realloc(*intensity, length_height * sizeof(double));
  (*length_intensity) = length_height;
  for (uint64_t i = 0; i < length_height; i++) {
    (*intensity)[i] = 80.0 * (1.0 + sin(2.0 * M_PI * time / 365.0)) / pow(fabs(200 - height[i]), 2);
  }
  return 0;
}
