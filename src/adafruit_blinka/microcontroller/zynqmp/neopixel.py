import time
import math
import atexit
from pynq import MMIO

# LED configuration.
NEOPIXEL_BASE_ADDRESS =         0x0080002000
NEOPIXEL_MEM_SIZE =             1024
NEOPIXEL_COUNT_REG_OFFSET =     0x0
NEOPIXEL_REG_0_OFFSET =         0x4

NEOPIXEL_COUNT =                0x1

# a 'static' object that we will use to manage our neopixel controller IP
# we only support one LED strip per raspi
_neopixel_controller = None

def neopixel_cleanup():
    global _neopixel_controller
    if _neopixel_controller is not None:
        _neopixel_controller = None


def neopixel_write(gpio, buf):

    global _neopixel_controller # we'll have one controller we init if its not at first

    if _neopixel_controller is None:

        _neopixel_controller = MMIO(NEOPIXEL_BASE_ADDRESS, NEOPIXEL_MEM_SIZE)
        _neopixel_controller.write(NEOPIXEL_COUNT_REG_OFFSET, NEOPIXEL_COUNT)

    bpp = 3
    for i in range(len(buf) // bpp):
        r = buf[bpp*i]
        g = buf[bpp*i+1]
        b = buf[bpp*i+2]
        if bpp == 3:
            pixel = (r << 16) | (g << 8) | b

        _neopixel_controller.write(NEOPIXEL_REG_0_OFFSET + (0x4 * i), pixel)

    time.sleep(0.001 * ((len(buf)//100)+1))  # about 1ms per 100 bytes
