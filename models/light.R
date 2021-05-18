
light <- function(height, time) {
  intensity <- 80.0 * (1.0 + sin(2.0 * pi *
    units::drop_units(time / units::set_units(365, 'days')))) /
    (abs(200 - height)**2)
  return(intensity)
}