from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin

GPIO_0 = Pin((338, 36))
GPIO_1 = Pin((338, 37))
GPIO_2 = Pin((338, 39))
GPIO_3 = Pin((338, 40))
GPIO_4 = Pin((338, 44))
GPIO_5 = Pin((338, 45))

GPIO_6 = Pin((338, 78))
GPIO_7 = Pin((338, 79))
GPIO_8 = Pin((338, 80))
GPIO_9 = Pin((338, 81))
GPIO_10 = Pin((338, 82))
GPIO_11 = Pin((338, 83))

GPIO_12 = Pin((338, 4))
GPIO_13 = Pin((338, 5))

I2C1_SDA = GPIO_13
I2C1_SCL = GPIO_12

i2cPorts = ((1, I2C1_SCL, I2C1_SDA), )
