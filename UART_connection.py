import serial
import threading

BAUD_RATE = 115200
PORT = "//./COM4"
PARITY = serial.PARITY_EVEN
DATA_SIZE = serial.EIGHTBITS
STOP_BITS = serial.STOPBITS_ONE


class UARTConnection:
    def __init__(self):
        self.connection = serial.Serial()  # Create a new serial instance
        self.connection.port = PORT
        self.connection.baudrate = BAUD_RATE
        self.connection.parity = PARITY
        self.connection.bytesize = DATA_SIZE
        self.connection.stopbits = STOP_BITS
        self.connection.open()  # Create the serial connection
        read_poll_thread = threading.Thread(target=self.poll_read_UART)
        read_poll_thread.start()
        curr_state = 0

    def poll_read_UART(self):
        while True:
            data = self.connection.read()
            curr_state = int()

    def send_UART(self, msg):
        self.connection.write(msg.decode("utf-8"))


if __name__ == "__main__":
    uart = UARTConnection()
