#' Compute the intensity of light.
#'
#' @param doy Day of year.
#' @param height Distance from ground in cm.
#'
#' @return Intensity of light in ergs cm^-2 s^-1.
light <- function(doy, height) {
  # Define parameters that are static across a run
  amplitude <- units::set_units(80.0, 'ergs cm-3 s-1')
  doy_offset <- units::set_units(0.0, 'days')

  # Calculate intensity
  intensity <- amplitude * height * (1.0 + sin(2.0 * pi *
    units::drop_units((doy - doy_offset) / units::set_units(365, 'days'))))
  return(intensity)
}