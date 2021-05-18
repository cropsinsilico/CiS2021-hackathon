function light(height, time, intensity) result(out)
  real(kind=8), dimension(:), intent(in) :: height
  real(kind=8), intent(in) :: time
  real(kind=8), dimension(:), allocatable :: intensity
  logical :: out
  integer :: i
  real, parameter :: Pi = 3.1415927
  out = .true.
  if (allocated(intensity)) then
     deallocate(intensity)
  end if
  allocate(intensity(size(height)))
  do i = 1, size(height)
     intensity(i) = 80.0 * (1.0 + SIN(2.0 * Pi * time / 365)) / (ABS(200.0 - height(i))**2)
  end do
end function light
