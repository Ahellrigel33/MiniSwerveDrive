from inputs import get_gamepad
import math
import threading
import serial
import serial.tools.list_ports
import http
import time
import urllib.request

ports = serial.tools.list_ports.comports()

url_esp8266 = "http://192.168.137.49/"  # ESP's IP, ex: http://192.168.102/ (Check serial console while uploading the ESP code, the IP will be printed)
update_interval = .005 # (seconds) how often XBox controller data is sent over Wi-Fi to 


# debugging function to list all connected comports
def list_all_comports():
    for port in list(ports):
        print("--------------------------")
        print(str(port) + ':')
        print("hid: " + port.hwid)
        print("name: " + port.name)
        print("device: " + port.device)
        print("desc: " + port.description)
        print("vid: " + port.vid)
        print("pid: " + port.pid)
        print("serial number: " + port.serial_number)
        print("location: " + port.location)
        print("interface: " + port.interface)
        print("product: " + port.product)
        print("manufacturer: " + port.manufacturer)
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


    def read(self): # return the relevant buttons/triggers
        return [str(self.LeftJoystickX), str(self.LeftJoystickY), str(self.RightJoystickX)]

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

# Sends XBox controller data over Wi-Fi to the specificed url
def send_control_data(controller, url):
    out_cmd = "_".join(controller.read())
    transfer(out_cmd)
    print(out_cmd)
    
# send and receive data over Wi-Fi
def transfer(my_url):   
    try:
        n = urllib.request.urlopen(url_esp8266 + my_url).read()
        n = n.decode("utf-8")
        return n
    except http.client.HTTPException as e:
        # print("HTTP Exception")
        return e


if __name__ == '__main__':
    controller = XboxController()
    # mbed = serial.Serial(find_bluetooth_comport(desc = 'mbed'), 9600, timeout = 1, write_timeout = 1)  # open serial port for mbed
    
    print("Starting XBox controller data transfer over Wi-Fi to ESP8266...")
    prev_execute_time = time.time()
    while True:
        if ((time.time() - prev_execute_time) > update_interval):
            send_control_data(controller, url_esp8266)
            prev_execute_time = time.time()