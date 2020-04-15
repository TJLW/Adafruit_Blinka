from pynq import GPIO

# Pins dont exist in CPython so...lets make our own!
class Pin:
    IN = 0
    OUT = 1
    LOW = 0
    HIGH = 1
    PULL_NONE = 0
    PULL_UP = 1
    PULL_DOWN = 2

    id = None
    _value = LOW
    _mode = IN

    pynq_gpio = None

    def __init__(self, pin_id):
        self.id = pin_id

    def __repr__(self):
        return str(self.id)

    def __eq__(self, other):
        return self.id == other

    def init(self, mode=None, pull=None):
        if mode != None:
            if mode == self.IN:
                self._mode = self.IN
                # GPIO.setup(self.id, GPIO.IN)
                if self.pynq_gpio == None:
                    self.pynq_gpio = GPIO(self.id, 'in')
                else:
                    self.pynq_gpio.direction = 'in'
            elif mode == self.OUT:
                self._mode = self.OUT
                # GPIO.setup(self.id, GPIO.OUT)
                if self.pynq_gpio == None:
                    self.pynq_gpio = GPIO(self.id, 'out')
                else:
                    self.pynq_gpio.direction = 'out'
            else:
                raise RuntimeError("Invalid mode for pin: %s" % self.id)
        # if pull != None:
        #     if self._mode != self.IN:
        #         raise RuntimeError("Cannot set pull resistor on output")
        #     if pull == self.PULL_UP:
        #         GPIO.setup(self.id, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #     elif pull == self.PULL_DOWN:
        #         GPIO.setup(self.id, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #     else:
        #         raise RuntimeError("Invalid pull for pin: %s" % self.id)

    def value(self, val=None):
        if val != None:
            if val == self.LOW:
                self._value = val
                # GPIO.output(self.id, val)
                self.pynq_gpio.write(val)
            elif val == self.HIGH:
                self._value = val
                # GPIO.output(self.id, val)
                self.pynq_gpio.write(val)
            else:
                raise RuntimeError("Invalid value for pin")
        else:
            # return GPIO.input(self.id)
            return self.pynq_gpio.read()

# from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin
#
GPIO_0 = Pin(374)
GPIO_1 = Pin(375)
GPIO_2 = Pin(377)
GPIO_3 = Pin(378)
GPIO_4 = Pin(382)
GPIO_5 = Pin(383)

GPIO_6 = Pin(416)
GPIO_7 = Pin(417)
GPIO_8 = Pin(418)
GPIO_9 = Pin(419)
GPIO_10 = Pin(420)
GPIO_11 = Pin(421)

GPIO_12 = Pin(342)
GPIO_13 = Pin(343)

I2C1_SDA = GPIO_13
I2C1_SCL = GPIO_12

i2cPorts = ((2, I2C1_SCL, I2C1_SDA), )
