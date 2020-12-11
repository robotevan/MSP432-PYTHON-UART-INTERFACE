import serial
import threading
from os import system

BAUD_RATE = 115200
PORT = "//./COM4"
PARITY = serial.PARITY_EVEN
DATA_SIZE = serial.EIGHTBITS
STOP_BITS = serial.STOPBITS_ONE

NEXT_STATE = b'a'
PREV_STATE = b'b'


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
        self.curr_state = 0
        self.read_thread = threading.Thread(target=self.poll_read_UART)
        self.read_thread.start()

    def _print_menu(self):
        print("_______________________________________________________")
        print("|   Start by entering one of the following commands:  |\n"
              "|       -next: go to next state                       |\n"
              "|       -prev: go to previous state                   |\n"
              "|-----------------------------------------------------|\n"
              "|    Current State: " + str(self.curr_state) +"                                 |\n"
              "|-----------------------------------------------------|\n")


    def poll_read_UART(self):
        while True:
            data = self.connection.read()
            if data == b'c':
                self.curr_state = 0
            elif data == b'd':
                self.curr_state = 1
            elif data == b'd':
                self.curr_state = 2
            elif data == b'e':
                self.curr_state = 3


    def main_thread(self):
        while True:
            #self._print_menu()
            print(self.curr_state)
            #system("cls")
            msg = input("Enter a command: ")
            if msg == "next":
                self.connection.write(NEXT_STATE)
            elif msg == "prev":
                self.connection.write(PREV_STATE)
            else:
                print("INVALID STATE!")




if __name__ == "__main__":
    uart = UARTConnection()
    uart.main_thread()