import serial

class ArduinoDevice:
    serial_device = None

    def __init__(self, device = '/dev/tty.usbserial-A105OIEB', baudrate = 19200):
        self.serial_device = serial.Serial(device, baudrate)

    def recv(self, amount = -1):
        data = b''
        if amount > 0:
            data = self.serial_device.read(amount)
        else:
            chars_available = self.serial_device.in_waiting
            while chars_available:
                data += self.serial_device.read(chars_available)
                chars_available = self.serial_device.in_waiting
        return data

    def send(self, data):
        self.serial_device.write(data + b'\r\n')
        self.serial_device.flush()

    def send_line(self, data):
        self.send(data + b'\r\n')

