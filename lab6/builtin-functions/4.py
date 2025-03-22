import math
import time

# Take inputs
number = int(input())        # e.g. 25100
delay_ms = int(input())      # e.g. 2123

# Wait for delay in seconds (milliseconds ÷ 1000)
time.sleep(delay_ms / 1000)

# Calculate square root using built-in function
result = math.sqrt(number)

# Print the output
print(f"Square root of {number} after {delay_ms} miliseconds is {result}")