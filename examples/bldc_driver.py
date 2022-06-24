from machine import Pin, PWM
import math
import time


# used led for better debugging
led = Pin(25, Pin.OUT)  # RPI Pico built in LED
led.on()

############################################################
# Note: all following service pins are inverted            #
#       therefore the 'n' meaning 'not' before their names #
############################################################
nFault = Pin(6, Pin.IN)   # not-Fault input

nSleep = Pin(7, Pin.OUT)  # not-Sleep output
nSleep.on()               # set to on to not activate sleep mode

nReset = Pin(8, Pin.OUT)  # not-Reset output
nReset.on()               # set to on to not reset the driver


# definition of enable and PWM pins
en = Pin(5, Pin.OUT)  # enable pin
en.on()               # set to on to enable the driver

pwm0 = PWM(Pin(2))    # PWM phase 1 pin
pwm0.freq(20000)      # frequency set to 20kHz (above the audible range)

pwm1 = PWM(Pin(3))    # PWM phase 2 pin
pwm1.freq(20000)

pwm2 = PWM(Pin(4))    # PWM phase 3 pin
pwm2.freq(20000)


##############################
# Custom Parameters          #
# adapt these to your needs! #
##############################
n = 1.0     # number of motor rotations
pp = 7      # number motor of pole pairs
pv = 1.0    # percent of input voltage (e.g. input is 24V; motor needs 12V; -> pv=0.5)
res = 200   # resolutoin/steps per field rotation


# definition of some constants and variables
step = (2*math.pi)/res  # step angle; amount of which the field angle is increased every loop
scale = 0.5*pv          # scaling factor for the sine wave
phi = 0.0               # angle of the electromagnetc field

# main loop
for i in range(int(n*pp*res)):
    phi = phi + step
    
    a = 65535 * (scale * math.sin(phi) + 0.5)
    b = 65535 * (scale * math.sin(phi+2.094395) + 0.5)
    c = 65535 * (scale * math.sin(phi+4.188790) + 0.5)
    
    pwm0.duty_u16(int(a))
    pwm1.duty_u16(int(b))
    pwm2.duty_u16(int(c))
    
    time.sleep_ms(1)  # adjust rotation speed


# after the loop finished after n number of rotations
en.off()   # turn off the motor driver
led.off()  # turn of the led