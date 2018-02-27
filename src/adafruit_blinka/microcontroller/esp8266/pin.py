from microcontroller import Pin

GPIO0 = Pin(0)
GPIO1 = Pin(1)
GPIO2 = Pin(2)
GPIO3 = Pin(3)
GPIO4 = Pin(4)
GPIO5 = Pin(5)
GPIO12 = Pin(12)
GPIO13 = Pin(13)
GPIO14 = Pin(14)
GPIO15 = Pin(15)
GPIO16 = Pin(16)
TOUT = Pin("TOUT")

# ordered as spiId, sckId, mosiId, misoId
spiPorts = ((1, GPIO14, GPIO13, GPIO12))

# ordered as uartId, txId, rxId
uartPorts = (
    (0, GPIO1, GPIO3),
    # (0, GPIO15, GPIO13) # TODO secondary pins for UART0 configurable from Micropython? How to flag?
    (1, GPIO2, None))

i2cPorts = ()