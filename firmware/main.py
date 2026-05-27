import machine
from machine import Pin
from neopixel import NeoPixel
from time import sleep

batt_sense = Pin(15, Pin.IN)
_leds_mainboard = Pin(0, Pin.OUT)
leds_mainboard = NeoPixel(_leds_mainboard, 6)

_leds_f1 = Pin(1, Pin.OUT)
leds_f1 = NeoPixel(_leds_f1, 2)
_leds_f2 = Pin(2, Pin.OUT)
leds_f2 = NeoPixel(_leds_f2, 2)
_leds_f3 = Pin(3, Pin.OUT)
leds_f3 = NeoPixel(_leds_f3, 2)
_leds_f4 = Pin(4, Pin.OUT)
leds_f4 = NeoPixel(_leds_f4, 2)

i2c_mplx_cl = Pin(47, Pin.OUT)
i2c_mplx_da = Pin(48)

i = 0
while True:
    for _ in range(6):
        leds_mainboard[_] = [i,i,i]
    leds_mainboard.write()
    for _ in range(2):
        leds_f1[_] = [i,i,i]
        leds_f2[_] = [i,i,i]
        leds_f3[_] = [i,i,i]
        leds_f4[_] = [i,i,i]

    leds_f1.write()
    leds_f2.write()
    leds_f3.write()
    leds_f4.write()
    i += 4
    i %= 256
    
    sleep(0.01)
