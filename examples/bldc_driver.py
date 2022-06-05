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

u = 7    # Anzahl der Feldumdrehungen
p = 1.0  # Prozent der max. Spannung

scale = 0.5*p
phi = 0.0

for i in range(200*u):
    phi = phi + 0.031415
    
    a = 65535 * (scale * math.sin(phi) + 0.5)
    b = 65535 * (scale * math.sin(phi+2.094395) + 0.5)
    c = 65535 * (scale * math.sin(phi+4.188790) + 0.5)
    
    pwm0.duty_u16(int(a))
    pwm1.duty_u16(int(b))
    pwm2.duty_u16(int(c))
    
    time.sleep_ms(1)


en.off()
led.off()  