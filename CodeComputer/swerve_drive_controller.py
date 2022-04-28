from black import out
from inputs import get_gamepad
import math
import threading
import serial
import serial.tools.list_ports
import struct
import time
ports = serial.tools.list_ports.comports()

hid_bluetooth = "002106BE9A97"
# hid_mbed

def list_all_comports():
    for port in list(ports):
        print("--------------------------")
        print(str(port) + ':')
        print("hid: " + port.hwid)
        print(port.name)
        print("device: " + port.device)
        print("desc: " + port.description)
        print(port.vid)
        print(port.pid)
        print(port.serial_number)
        print(port.location)
        print(port.interface)
        print(port.product)
        print(port.manufacturer)
        print("--------------------------")

class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):

        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()


    def read(self): # return the buttons/triggers that you care about in this methode
        # x = self.LeftJoystickX
        # y = self.LeftJoystickY
        # a = self.A
        # b = self.X # b=1, x=2
        # rb = self.RightBumper
        # return [x, y, a, b, rb]
        return [self.LeftJoystickX, self.LeftJoystickY, self.RightJoystickX]
        print(
        self.LeftJoystickY,
        self.LeftJoystickX,
        self.RightJoystickY,
        self.RightJoystickX,
        self.LeftTrigger,
        self.RightTrigger,
        self.LeftBumper,
        self.RightBumper,
        self.A,
        self.X,
        self.Y,
        self.B,
        self.LeftThumb,
        self.RightThumb,
        self.Back,
        self.Start,
        self.LeftDPad,
        self.RightDPad,
        self.UpDPad,
        self.DownDPad)


    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.X = event.state
                elif event.code == 'BTN_WEST':
                    self.Y = event.state
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY1':
                    self.LeftDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY2':
                    self.RightDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY3':
                    self.UpDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY4':
                    self.DownDPad = event.state

def find_bluetooth_comport(hid = None, desc = None):
    for port in list(ports):
        if hid:
            if hid in port.hwid:
                # print("Desired bluetooth device found")
                print(str(port) + ':')
                # print(port.hwid)
                # print(port.device)
                return port.device
        if desc:
            if desc in port.description:
                # print("Desired bluetooth device found")
                print(str(port) + ':')
                # print(port.hwid)
                # print(port.device)
                return port.device
    print("Connection not found")

def send_control_data(controller, serial_device):
    
    l_joy_x, l_joy_y, r_joy_x = controller.read()
    out_cmd = struct.pack('fff', l_joy_x, l_joy_y, r_joy_x)
    serial_device.write(b'a')
    num_bytes = serial_device.write(out_cmd)
    # print("{} bytes: {}".format(num_bytes, out_cmd))
    # print("{} bytes: {}".format(num_bytes, struct.unpack('fff',out_cmd)))
    
    
update_interval = .1 # seconds

if __name__ == '__main__':
    list_all_comports()
    read_str = ""
    controller = XboxController()
    mbed = serial.Serial(find_bluetooth_comport(desc = 'mbed'), 9600, timeout = 1, write_timeout = 1)  # open serial port
    # bt = serial.Serial(find_bluetooth_comport(hid = hid_bluetooth), 9600)  # open serial port
    

    print("Starting...")
    prev_execute_time = time.time()
    while True:
        if ((time.time() - prev_execute_time) > update_interval):
            a = send_control_data(controller, mbed)
            prev_execute_time = time.time()