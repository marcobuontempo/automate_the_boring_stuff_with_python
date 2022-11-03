#! python3
# prettified_stopwatch.py - A simple stopwatch program, with "prettified" outputs and each output also saved to clipboard.

import time, pyperclip

# Display the program's instructions
print("Press ENTER to begin. Afterwards, press ENTER to 'click' the stopwatch. Press Ctrl-C to quit.")
input() # Press Enter to begin
print("Started.")
start_time = time.time()    # Get the first lap's start time
last_time = start_time
lap_num = 1

# Start tracking the lap times.
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        output_text = "Lap #%s: %ss (%ss)" % (str(lap_num).rjust(2), str(total_time).rjust(6), str(lap_time).rjust(6))
        print(output_text, end="")  # Print to console
        pyperclip.copy(output_text) # Save output to clipboard
        lap_num += 1
        last_time = time.time() # Reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print("\nDone.")