from picozero import OutputDevice
import sys
import select
from time import sleep

# Initialize Relays
relay1 = OutputDevice(7)
relay2 = OutputDevice(8)

# Set up the console poll (Non-blocking standard input)
poll_obj = select.poll()
poll_obj.register(sys.stdin, select.POLLIN)

print("System ready. Type '1' for Relay 1, '2' for Relay 2, '0' for OFF. Press Enter.")
print("Press Ctrl+C to stop.")

def check_user_input():
    # poll(0) checks immediately and returns without waiting
    if poll_obj.poll(0):
        # Read the character the user typed
        char = sys.stdin.readline().strip()
        
        if char == '1':
            relay1.toggle()
            print("Relay 1 ->", "ON" if relay1.is_active else "OFF")
        elif char == '2':
            relay2.toggle()
            print("Relay 2 ->", "ON" if relay2.is_active else "OFF")
        elif char == '0':
            relay1.off()
            relay2.off()
            print("All Relays -> OFF")

try:
    # Main program loop
    while True:
        # 1. Check for user keyboard input
        check_user_input()
        
        # 2. Do your other tasks here (e.g., read sensors, update LCD)
        # We use a tiny sleep just to prevent the loop from maxing out the CPU 100%
        sleep(0.1)

except KeyboardInterrupt:
    relay1.off()
    relay2.off()
    print("\nSystem halted.")
