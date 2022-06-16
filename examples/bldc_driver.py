from machine import Pin, PWM
import math
import time


led = Pin(25, Pin.OUT)
led.on()

en = Pin(5, Pin.OUT)
en.on()

pwm0 = PWM(Pin(2))
pwm0.freq(20000)

pwm1 = PWM(Pin(3))
pwm1.freq(20000)

pwm2 = PWM(Pin(4))
pwm2.freq(20000)

n = 1.0     # number of motor rotations
pp = 7      # number motor of pole pairs
pv = 1.0    # percent of input voltage
res = 200   # resolutoin/steps per field rotation

scale = 0.5*pv
phi = 0.0

for i in range(int(n*pp*res)):
    phi = phi + (2*math.pi)/res
    
    a = 65535 * (scale * math.sin(phi) + 0.5)
    b = 65535 * (scale * math.sin(phi+2.094395) + 0.5)
    c = 65535 * (scale * math.sin(phi+4.188790) + 0.5)
    
    pwm0.duty_u16(int(a))
    pwm1.duty_u16(int(b))
    pwm2.duty_u16(int(c))
    
    time.sleep_ms(1)  # adjust rotation speed


en.off()
led.off()  