#define _USE_MATH_DEFINES  // Required to use M_PI with MSVC
#include <math.h>

/*!
  @brief Compute the intensity of light.

  @param[in] doy Day of year.
  @param[in] height Distance from ground in cm.

  @returns intensity Intensity of light in ergs cm^-2 s^-1.
 */
double light(double doy, double height) {
  // Define parameters that are static across a run
  double amplitude = 80.0;
  double doy_offset = 0.0;

  // Calculate intensity
  double intensity = amplitude * height * (1.0 + sin(2.0 * M_PI * (doy - doy_offset) / 365));
  
  return intensity;
}
