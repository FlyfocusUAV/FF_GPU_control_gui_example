from FF_GPU_control_gui_example import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
import time
import socket

def loop():
    global ui
    values = {}
    while(1):
        #Send request for telemetry values to the GPU
        sock.settimeout(1)

        #Check if we received something or the timeout exception was thrown
        try:
            sock.sendto(REQUEST_MESSAGE.encode(), (UDP_IP, UDP_PORT))
            data, addr = sock.recvfrom(1024)
            
            #print("Received data: %s" % data)
            #print("Received data: %s" % data.decode("utf-8"))

            #Incoming data parser
            data_str = data.decode("utf-8")
            lines = data_str.split("\r\n")
            for line in lines:
                parts = line.split(": ")
                if(len(parts) >= 2):
                    values[parts[0]] = parts[1]

            
            print("Received Heartbeat Status[OK/FAULT]:", values["HRTBT"])
            print("Received Output State[SAFE/HV!/UNKNOWN]:", values["OUTPUT STATE"])
            print("Received Cable Tension[g]:", values["CABLE TENSION"])
            print("Received Cable Length[m]:", values["CABLE LENGTH"])
            print("Received Output Power[W]:", values["POWER W"])
            print("Received Mains Status[ON/OFF]:", values["MAINS"])
            print("\n\r")

            ui.StatusHrtbtLabel.setText("HEARTBEAT: " + values["HRTBT"])
            ui.StatusOutputStateLabel.setText("OUTPUT: " + values["OUTPUT STATE"])
            ui.StatusTensionLabel.setText("TENSION[g]: " + values["CABLE TENSION"])
            ui.StatusCableLenLabel.setText("CABLE LEN[m]: " + values["CABLE LENGTH"])
            ui.StatusPwrLabel.setText("POWER[W]: " + values["POWER W"])
            ui.StatusMainsLabel.setText("MAINS: " + values["MAINS"])
            
            

        except socket.timeout:
            print("No response from GPU")
            ui.StatusHrtbtLabel.setText("HEARTBEAT: NO GPU")
            time.sleep(0.1)
        
        except OSError:
            print("network unreachable")
            ui.StatusHrtbtLabel.setText("HEARTBEAT: ERROR")
            time.sleep(0.1)


        time.sleep(0.2)
        



def callbackOnButton():
    global ui
    sock.sendto(ON_MESSAGE.encode(), (UDP_IP, UDP_PORT))

def callbackOffButton():
    global ui
    sock.sendto(OFF_MESSAGE.encode(), (UDP_IP, UDP_PORT))

def callbackTensionSetButton():
    global ui
    val = ui.TensionSpinBox.value()
    TNS_SET_MESSAGE = "#TNS" + str(val).zfill(4) + '\r'
    #print(TNS_SET_MESSAGE)
    sock.sendto(TNS_SET_MESSAGE.encode(), (UDP_IP, UDP_PORT))

def callbackTensionZeroButton():
    global ui
    val = 0
    TNS_SET_MESSAGE = "#TNS" + str(val).zfill(4) + '\r'
    #print(TNS_SET_MESSAGE)
    sock.sendto(TNS_SET_MESSAGE.encode(), (UDP_IP, UDP_PORT))

def callbackBrakeOnButton():
    global ui
    sock.sendto(BRAKE_ON_MESSAGE.encode(), (UDP_IP, UDP_PORT))

def callbackBrakeOffButton():
    global ui
    sock.sendto(BRAKE_OFF_MESSAGE.encode(), (UDP_IP, UDP_PORT))


def initialSetup(ui):
    ui.OnSetButton.clicked.connect(callbackOnButton)
    ui.OffSetButton.clicked.connect(callbackOffButton)
    ui.TensionSetButton.clicked.connect(callbackTensionSetButton)
    ui.TensionZeroButton.clicked.connect(callbackTensionZeroButton)
    ui.BrakeOnButton.clicked.connect(callbackBrakeOnButton)
    ui.BrakeOffButton.clicked.connect(callbackBrakeOffButton)


if __name__ == "__main__":

    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    initialSetup(ui)

    UDP_IP = "192.168.1.200"
    UDP_PORT = 6543
    REQUEST_MESSAGE = "#RQ\r"
    ON_MESSAGE = "#ON\r"
    OFF_MESSAGE = "#OFF\r"
    BRAKE_ON_MESSAGE = "#B_ON\r"
    BRAKE_OFF_MESSAGE = "#B_OFF\r"
    print("UDP target IP: %s" % UDP_IP)
    print("UDP target port: %s" % UDP_PORT)
    print("Request message: %s" % REQUEST_MESSAGE)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#args=(ui,),
    t = Thread(target=loop,  daemon=True)
    t.start()


    MainWindow.show()
    sys.exit(app.exec_())
