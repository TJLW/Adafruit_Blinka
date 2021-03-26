import time
import math
import atexit
import mmap
import os
# from pynq import MMIO

# LED configuration.
NEOPIXEL_BASE_ADDRESS =         0x0080000000
NEOPIXEL_MEM_SIZE =             2048
NEOPIXEL_COUNT_REG_OFFSET =     0x0
NEOPIXEL_REG_0_OFFSET =         0x4

NEOPIXEL_COUNT =                0x1

NUM_PIXEL_OFFSET = 0
PIXELS_OFFSET = 4

RED_OFFSET = 0
GREEN_OFFSET = 1
BLUE_OFFSET = 2

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

        devmem = os.open("/dev/mem", os.O_RDWR | os.O_SYNC | os.O_CREAT)
        _neopixel_controller = mmap.mmap(devmem, NEOPIXEL_MEM_SIZE, flags = mmap.MAP_SHARED, prot = mmap.PROT_WRITE | mmap.PROT_READ, offset = NEOPIXEL_BASE_ADDRESS)

        _neopixel_controller.seek(NUM_PIXEL_OFFSET)
        _neopixel_controller.write_byte(NEOPIXEL_COUNT)

        # _neopixel_controller = MMIO(NEOPIXEL_BASE_ADDRESS, NEOPIXEL_MEM_SIZE)
        # _neopixel_controller.write(NEOPIXEL_COUNT_REG_OFFSET, NEOPIXEL_COUNT)

    bpp = 3
    for i in range(len(buf) // bpp):
        r = buf[bpp*i]
        g = buf[bpp*i+1]
        b = buf[bpp*i+2]
        if bpp == 3:
            # pixel = (r << 16) | (g << 8) | b
            _neopixel_controller.seek(PIXELS_OFFSET + RED_OFFSET)
            _neopixel_controller.write_byte(r)

            _neopixel_controller.seek(PIXELS_OFFSET + GREEN_OFFSET)
            _neopixel_controller.write_byte(g)

            _neopixel_controller.seek(PIXELS_OFFSET + BLUE_OFFSET)
            _neopixel_controller.write_byte(b)


        # _neopixel_controller.write(NEOPIXEL_REG_0_OFFSET + (0x4 * i), pixel)

    time.sleep(0.001 * ((len(buf)//100)+1))  # about 1ms per 100 bytes
