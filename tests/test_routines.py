from climate_network.routines import fib, factorial, array_stats

# Get first 10 Fibonacci numbers
print(fib.__doc__)
fib_array = fib(10)
print("Fibonacci numbers:", fib_array)

# Calculate factorial of 5
print(factorial.__doc__)
fact_result = factorial(5)
print("5! =", fact_result)

# Calculate statistics on the Fibonacci array
print(array_stats.__doc__)
mean, max_val, min_val, std_dev = array_stats(fib_array, len(fib_array))
print(f"Stats: mean={mean}, max={max_val}, min={min_val}, std_dev={std_dev}")
