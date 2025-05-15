subroutine fib(a, n)
    integer, intent(in) :: n
    real(8), intent(out), dimension(n) :: a
    !f2py intent(in) n
    !f2py intent(out) a
    !f2py depend(n) a
    !f2py doc: a = fib(n) -- Returns the first n Fibonacci numbers in array a
    integer :: i

    do i = 1, n
        if (i == 1) then
            a(i) = 0.0d0
        else if (i == 2) then
            a(i) = 1.0d0
        else
            a(i) = a(i-1) + a(i-2)
        endif
    end do
end subroutine fib

subroutine factorial(n, result)
    integer, intent(in) :: n
    real(8), intent(out) :: result
    !f2py intent(in) n
    !f2py intent(out) result
    !f2py doc: result = factorial(n) -- Returns the factorial of n
    integer :: i

    result = 1.0d0
    do i = 2, n
        result = result * i
    end do
end subroutine factorial

subroutine array_stats(a, n, mean, max_val, min_val, std_dev)
    integer, intent(in) :: n
    real(8), intent(in), dimension(n) :: a
    real(8), intent(out) :: mean, max_val, min_val, std_dev
    !f2py intent(in) a
    !f2py intent(in) n
    !f2py intent(out) mean
    !f2py intent(out) max_val
    !f2py intent(out) min_val
    !f2py intent(out) std_dev
    !f2py depend(n) a
    !f2py doc: mean, max, min, std = array_stats(a, n) -- Calculates basic statistics for array a
    integer :: i
    real(8) :: sum_squares

    ! Calculate mean
    mean = 0.0d0
    do i = 1, n
        mean = mean + a(i)
    end do
    if (n > 0) then
        mean = mean / n
    end if

    ! Find max and min
    if (n > 0) then
        max_val = a(1)
        min_val = a(1)
        do i = 2, n
            if (a(i) > max_val) max_val = a(i)
            if (a(i) < min_val) min_val = a(i)
        end do
    else
        max_val = 0.0d0
        min_val = 0.0d0
    end if

    ! Calculate standard deviation
    sum_squares = 0.0d0
    do i = 1, n
        sum_squares = sum_squares + (a(i) - mean)**2
    end do
    if (n > 1) then
        std_dev = sqrt(sum_squares / (n - 1))
    else
        std_dev = 0.0d0
    end if
end subroutine array_stats

