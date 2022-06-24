# DRV8313-Breakout
This is an unofficial Breakout Board for the <a href="https://www.ti.com/product/DRV8313" target="_blank" rel="noopener noreferrer">Texas-Instruments DRV8313 Triple-Half-Bridge Motor Driver IC</a>

## <a href="https://www.ebay.de/itm/384936164923?hash=item599ffbbe3b:g:I74AAOSwUhFin4ep" target="_blank" rel="noopener noreferrer">Where to get it?</a>
- <a href="https://www.ebay.de/itm/384936164923?hash=item599ffbbe3b:g:I74AAOSwUhFin4ep" target="_blank" rel="noopener noreferrer">eBay</a> (EU shipping only)
- more platforms may follow soon

## Specs
| Property                   | Value        |
|----------------------------|--------------|
| Input Voltage              | 8V - 48V     |
| Input Current (peak)       | 3A           |
| PWM Phase Inputs           | 3            |
| Enable Pin                 | 1            |
| Reset Pin                  | yes          |
| Sleep Pin                  | yes          |
| Fault Indication Pin       | yes          |
| Output Motor Phases        | 3            |
| Output to Supply Your MCU  | 3.3V         |


## Hardware
| PCB Top                                                   | PCB Bottom
|-----------------------------------------------------------|-----------------------------------------------------------------|
| ![PCB Top](documentation/images/DRV8313-Breakout-top.PNG) | ![PCB Bottom](documentation/images/DRV8313-Breakout-bottom.PNG) |

<br/><br/>

# Example with RaspberryPi Pico
In this simple example, the DRV8313 breakout board is used together with a <a href="https://www.raspberrypi.com/products/raspberry-pi-pico" target="_blank" rel="noopener noreferrer">RaspberryPi Pico</a> to drive a brushless gimbal motor in an open loop configuration. Open loop means that we have no feedback on the motor angle. The motor is driven similar to a stepper motor with open loop control.<br/>
Three 120° phase shifted sine waves are fed in via the PWM pins of the microcontroller. The DRV8313 motor driver now amplifies the incoming PWM signal and uses it to drive the motor.<br/>
The output voltage to the motor depends on the input voltage of the DRV8313 and the duty cycle of the PWM signal.

## Wireing
![Wireing](documentation/images/PiPico_Example_Schematic.PNG)

## MicroPython Code
```
from machine import Pin, PWM
import math
import time


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
```

<br/><br/>

# What's next?
If you want to go deeper into the topic of BLDC motor control, you should definitely check out the awesome <a href="https://docs.simplefoc.com" target="_blank" rel="noopener noreferrer">simpleFOC</a> project!<br/>
You can use this DRV8313 breakout board perfectly as a suitable <a href="https://docs.simplefoc.com/bldcdriver3pwm" target="_blank" rel="noopener noreferrer">BLDC motor driver</a>.
