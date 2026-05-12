from picozero import Pot, Motor
from time import sleep

# Setup Potentiometers on ADC pins
# GPIO 26 is ADC0, GPIO 29 is ADC3
pot1 = Pot(26)
pot2 = Pot(29)


Heater1 = Motor(forward=8, backward=9)
Heater2 = Motor(forward=10, backward=11)

print("System Initialized. Turn the potentiometers to control temperatures.")

while True:
    # Read values from potentiometers (returns a float between 0.0 and 1.0)
    temp1 = pot1.value #need datasheet to calibration
    temp2 = pot2.value
    
    Heater1.value = temp1
    Heater2.value = temp2
    
    # Small delay to keep the loop stable
    sleep(0.01)