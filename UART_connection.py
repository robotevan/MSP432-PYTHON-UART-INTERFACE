import serial
import threading
from os import system

BAUD_RATE = 115200
PORT = "COM4"
PARITY = serial.PARITY_NONE
DATA_SIZE = serial.EIGHTBITS
STOP_BITS = serial.STOPBITS_ONE

NEXT_STATE = b'a'
PREV_STATE = b'b'
CURR_STATE = b'c'  # Doesn't matter what this is, MSP echos state if not next/prev command

class UARTConnection:
    def __init__(self):
        self.connection = serial.Serial()  # Create a new serial instance
        self.connection.port = PORT
        self.connection.baudrate = BAUD_RATE
        self.connection.parity = PARITY
        self.connection.bytesize = DATA_SIZE
        self.connection.stopbits = STOP_BITS
        self.connection.open()  # Create the serial connection
        self.running = True
        self.curr_state = 0
        self.read_poll_thread = threading.Thread(target=self.poll_user_input)
        self.read_poll_thread.start()
        self.connection.write(CURR_STATE)
        self._print_menu()

    def _print_menu(self):
        system("cls")
        print("_______________________________________________________")
        print("|   Start by entering one of the following commands:  |\n"
              "|       -next: go to next state                       |\n"
              "|       -prev: go to previous state                   |\n"
              "|       - q  : quit the application                   |\n"
              "|-----------------------------------------------------|\n"
              "|    Current State: " + str(self.curr_state) +"                                 |\n"
              "|-----------------------------------------------------|\n"
              "\n Please Enter A Command:  ")

    def poll_user_input(self):
        while self.running:
            command = input()
            if command == "next":
                self.connection.write(NEXT_STATE)
            elif command == "prev":
                self.connection.write(PREV_STATE)
            elif command == "q":
                self.connection.close()
                self.running = False
                exit()
            else:
                print("INVALID STATE!")

    def main_thread(self):
        while self.running:
            new_state = int(self.connection.read(1).decode("utf-8"))
            if new_state == 0:
                self.curr_state = 0
            elif new_state == 1:
                self.curr_state = 1
            elif new_state == 2:
                self.curr_state = 2
            elif new_state == 3:
                self.curr_state = 3
            self._print_menu()


if __name__ == "__main__":
    uart = UARTConnection()
    uart.main_thread()