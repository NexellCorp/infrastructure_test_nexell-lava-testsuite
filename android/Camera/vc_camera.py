# Author: Benjamin Lim <benjamin@nexell.co.kr>
import os
import sys
import time
import subprocess

from subprocess import call
from com.dtmilano.android.viewclient import ViewClient, ViewNotFoundException
from com.dtmilano.android.adb.adbclient import AdbClient

device, serialno = ViewClient.connectToDeviceOrExit()
vc = ViewClient(device, serialno)

package_name = "com.android.camera2"
#sys.stdout.write ("Device Name : ")
os.system("adb shell getprop ro.product.model")

# Camera Test Common_List
COM_EXPOSURE_LIST = []
COM_SIZE_LIST = []
COM_WB_LIST = []
COM_SWITCH = []
COM_RECORD = []

## for Landscape touch position.
DRONE_EXPOSURE_LIST = [[440, 390, "EXPOSURE"], [330, 390, "-3"], [380, 360, "-2"], [435, 340, "-1"], [490, 330, "0"], [545, 345, "1"], [600, 360, "2"], [640, 390, "3"]]
DRONE_SIZE_LIST = [[490, 390], [515, 330]]
DRONE_WB_LIST = [[490, 390, "OPTION"], [570, 345, "WHITE BALANCE"], [375, 315, "INCANDESCENT"], [435, 300, "FLUORESCENT"], [490, 280, "AUTO"], [545, 300, "DAYLIGHT"], [600, 315, "CLOUDY"]]
DRONE_SWITCH = [540, 390]
DRONE_RECORD = [[770, 425, "PANORAMA"], [840, 425, "RECORDER"], [910, 425, "CAMERA"]]

def make_dir():
    # Make the result DIR
    now = time.localtime()
    cur_dir = os.path.realpath(os.path.dirname(__file__))
    target_dir = "/storage/sdcard0/DCIM/Camera"
    result_dir = cur_dir+"/%04d-%02d-%02d_%02d_%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
    os.mkdir(result_dir, 0777)


def del_target_result():
    target_dir = "/storage/sdcard0/DCIM/Camera"
    


def chk_target_bd():
    name = subprocess.Popen("adb shell getprop ro.product.model", shell=True, stdout=subprocess.PIPE)
    target_board = name.stdout.read()
    #print target_board
    
    if (target_board.find('drone') != -1):
        target_board = "DRONE"
        cnt_ex = len(DRONE_EXPOSURE_LIST)
        cnt_sz = len(DRONE_SIZE_LIST)
        cnt_wb = len(DRONE_WB_LIST)
        cnt_rc = len(DRONE_RECORD)
        
        for ex_i in range(0, cnt_ex):
            COM_EXPOSURE_LIST.append(DRONE_EXPOSURE_LIST[ex_i])
        for sz_i in range(0, cnt_sz):
            COM_SIZE_LIST.append(DRONE_SIZE_LIST[sz_i])
        for wb_i in range(0, cnt_wb): 
            COM_WB_LIST.append(DRONE_WB_LIST[wb_i])
        COM_SWITCH.append(DRONE_SWITCH[0])
        for rc_i in range(0, cnt_rc):
            COM_RECORD.append(DRONE_RECORD[rc_i])
        
    elif (target_board.find('pyxis') != -1):
        target_board = "PYXIS"
        ## To Do.. for pyxis
    
    elif (target_board.find('lynx') != -1):
        target_board = "LYNX"
        ## To Do.. for Lynx
    
    else:
        print "Unknown Device : ", target_board

    print "Target Board : ", target_board



def shutter(cnt, btn_capture):
    print ("Capture Test Start")

    try:
        for i in range(0, cnt):
            btn_capture.touch()
            print "Capture ", i+1
            time.sleep(1)
    except ViewNotFoundException:
        print "Can not find the shutter button! Please check the screen!"

    print("Capture Test End")
    print("")

    
def exposure(btn_menu, btn_capture):
    print ("Exposure Control Test Start")
#    print "COM_EXPOSURE_LIST : ", len(COM_EXPOSURE_LIST)

    try:
        for ex in range(1, len(COM_EXPOSURE_LIST)):
            print "Exposure ", COM_EXPOSURE_LIST[ex][2]
#        for ex in range(1, 2):
   
#            btn_menu = vc.findViewByIdOrRaise(package_name + ":id/menu")
            btn_menu.touch()
            time.sleep(1)
# Select Exposure function
            x = COM_EXPOSURE_LIST[0][0]
            y = COM_EXPOSURE_LIST[0][1]
            device.touch(x, y)
            time.sleep(1)
# Exposure Value
            x = COM_EXPOSURE_LIST[ex][0]
            y = COM_EXPOSURE_LIST[ex][1]
            device.touch(x, y)
            time.sleep(1)
            btn_capture.touch()
            time.sleep(1)
            ex=ex+1

    except ViewNotFoundException:
        run_result = "fail"
        print "Can not find the Exposure button! Please check the screen!"
        sys.exit(1)
        
# Set default value (Exposure = 0)
#    btn_menu = vc.findViewByIdOrRaise(package_name + ":id/menu")
    btn_menu.touch()
    time.sleep(1)
# Select Exposure function
    x = COM_EXPOSURE_LIST[0][0]
    y = COM_EXPOSURE_LIST[0][1]
    device.touch(x, y)
    time.sleep(1)
# Exposure = 0
    x = COM_EXPOSURE_LIST[4][0]
    y = COM_EXPOSURE_LIST[4][1]
    device.touch(x, y)
    time.sleep(1)
    print("Exposure Test End")
    print("")


def size_control(btn_menu, btn_capture):
    print ("Size Control")
    try:
#        btn_menu = vc.findViewByIdOrRaise(package_name + ":id/menu")
        btn_menu.touch()
        time.sleep(1)
# Select Option Function
        x = DRONE_SIZE_LIST[0][0]
        y = DRONE_SIZE_LIST[0][1]
        device.touch(x, y)
        time.sleep(1)
# Select SIZE Function
        x = DRONE_SIZE_LIST[1][0]
        y = DRONE_SIZE_LIST[1][1]
        device.touch(x, y)
        time.sleep(1)
         
    except ViewNotFoundException:
        run_result = "fail"
        print "Can not find the Size control button! Please check the screen!"
        sys.exit(1)


def white_balance(btn_menu, btn_capture):    
    print ("White Balance Control Test Start")
#    print "COM_WB_LIST : ", len(COM_WB_LIST)
    try:
#        print "List : ", len(DRONE_WB_LIST)
        for wb in range(2, len(DRONE_WB_LIST)):
#        for wb in range(1, 2):
            if(wb>1):
                print "White Balance : ", DRONE_WB_LIST[wb][2]
   
#            btn_menu = vc.findViewByIdOrRaise(package_name + ":id/menu")
            btn_menu.touch()
            time.sleep(1)
# Select Option function
            x = DRONE_WB_LIST[0][0]
            y = DRONE_WB_LIST[0][1]
            device.touch(x, y)
            time.sleep(1)
# Select White Balance Function
            x = DRONE_WB_LIST[1][0]
            y = DRONE_WB_LIST[1][1]
            device.touch(x, y)
            time.sleep(1)
# Select White Balance list
            x = DRONE_WB_LIST[wb][0]
            y = DRONE_WB_LIST[wb][1]
            device.touch(x, y)
            time.sleep(1)

            btn_capture.touch()
            time.sleep(1)
#            print "wb : ", wb
            
# Set to Default Value(AUTO)
#        btn_menu = vc.findViewByIdOrRaise(package_name + ":id/menu")
        btn_menu.touch()
# Select Option function
        x = DRONE_WB_LIST[0][0]
        y = DRONE_WB_LIST[0][1]
        device.touch(x, y)
        time.sleep(1)
# Select White Balance Function
        x = DRONE_WB_LIST[1][0]
        y = DRONE_WB_LIST[1][1]
        device.touch(x, y)
        time.sleep(1)
# Select AUTO
        x = DRONE_WB_LIST[4][0]
        y = DRONE_WB_LIST[4][1]
        device.touch(x, y)
        time.sleep(1)
                
        print "Set to default White Balance : ", DRONE_WB_LIST[4][2]

    except ViewNotFoundException:
        run_result = "fail"
        print "Can not find the Size control button! Please check the screen!"
        sys.exit(1)

    print("White Balance Control Test End")
    print("")


def select_cam(str, btn_select_cam):   # Recording Test
    try:
# Set to Record Function
        btn_select_cam.touch()
        time.sleep(2)
        if(str == "PANORAMA"):
            x = DRONE_RECORD[0][0]
            y = DRONE_RECORD[0][1]
            device.touch(x, y)
            print DRONE_RECORD[0][2], " Selected"
        elif(str == "RECORDER"):
            x = DRONE_RECORD[1][0]
            y = DRONE_RECORD[1][1]
            device.touch(x, y)
            print DRONE_RECORD[1][2], " Selected"
        elif(str == "CAMERA"):
            x = DRONE_RECORD[2][0]
            y = DRONE_RECORD[2][1]
            device.touch(x, y)
            print DRONE_RECORD[2][2], " Selected"
        else:
            print "Unknown Camera."
            sys.exit(1)
        print ("")
        time.sleep(1)

    except ViewNotFoundException:
        run_result = "fail"
        print "Exception in the select_cam function! Please check the screen!"
        sys.exit(1)


def record_cam(record_time, btn_select_cam, btn_capture):   # Recording Test
    try:
# Set to Record Function
        select_cam("RECORDER", btn_select_cam)
       
        print "Start Recording.. "
        btn_capture.touch() # Start Recording
        
        while(record_time != 0):
            print record_time
            time.sleep(1)
            record_time = record_time-1
        
        btn_capture.touch() # Stop Recording
        time.sleep(2)
        print""
        print("End Recording")

    except ViewNotFoundException:
        run_result = "fail"
        print "Can not record the Camera! Please check the screen!"
        sys.exit(1)

    
    print("Camera Record Success..")
    print("")    
    select_cam("CAMERA", btn_select_cam)
   
def cam_switch(btn_menu):
    try:
#        btn_menu = vc.findViewByIdOrRaise(package_name + ":id/menu")
        btn_menu.touch()
        time.sleep(1)
        
        x = DRONE_SWITCH[0]
        y = DRONE_SWITCH[1]
        device.touch(x, y)
        time.sleep(1)

    except ViewNotFoundException:
        run_result = "fail"
        print "Can not switch the Camera! Please check the screen!"
        sys.exit(1)

    print("Camera Switch Success..")
    print("")


def get_result(target_dir, result_dir):
    print "Camera Test result transfer in progress..."
    print target_dir, result_dir


def main():
    shutter_cnt = 3
    record_time = 10
    
#    make_dir()
    call(['./del_result.sh'])
    
    vc.dump()
    btn_capture = vc.findViewByIdOrRaise(package_name + ":id/shutter_button")
    btn_menu = vc.findViewByIdOrRaise(package_name + ":id/menu")
    btn_select_cam = vc.findViewByIdOrRaise(package_name + ":id/camera_switcher")
    
    chk_target_bd()
    
    select_cam("CAMERA", btn_select_cam)
    shutter(shutter_cnt, btn_capture) # Capture count
    
    exposure(btn_menu, btn_capture)   # Exposure Test
#    size_control(btn_menu, btn_capture)   # Resolution Test. Not Yet
    white_balance(btn_menu, btn_capture)   # White Balance Test
    record_cam(record_time, btn_select_cam, btn_capture)   # Recording Test

    cam_switch(btn_menu)
    shutter(shutter_cnt, btn_capture) # Capture count
    exposure(btn_menu, btn_capture)   # Exposure Test
#    size_control(btn_menu, btn_capture)   # Resolution Test. Not Yet
    white_balance(btn_menu, btn_capture)   # White Balance Test
    record_cam(record_time, btn_select_cam, btn_capture)   # Recording Test

    call(['./get_result.sh'])
    
if __name__ == '__main__':
    main()
