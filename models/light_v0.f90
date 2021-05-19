!---------------------------------------------------------------------------
!> @brief Compute the intensity of light.
!
!> @param[in] doy: Day of year.
!> @param[in] height: Distance from ground in cm.
!
!> @return intensity: Intensity of light in ergs cm^-2 s^-1.
!---------------------------------------------------------------------------
function light(doy, height) result(intensity)
  real(kind=8) :: doy
  real(kind=8) :: height
  real(kind=8) :: intensity
  real, parameter :: Pi = 3.1415927
  
  ! Define parameters that are static across a run
  real, parameter :: amplitude = 80.0
  real, parameter :: doy_offset = 0.0

  ! Calculate intensity
  intensity = amplitude * height * (1.0 + SIN(2.0 * Pi * (doy - doy_offset) / 365))
end function light
