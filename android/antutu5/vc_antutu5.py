import re
import sys
import os
import time
from subprocess import call

from com.dtmilano.android.viewclient import ViewClient, ViewNotFoundException

kwargs1 = {'verbose': False, 'ignoresecuredevice': False}
device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)
kwargs2 = {'startviewserver': True, 'forceviewserveruse': False, 'autodump': False, 'ignoreuiautomatorkilled': True}
vc = ViewClient(device, serialno, **kwargs2)

#Wait while application loads
time.sleep(2)

print ("test")
"""
# Error Check
vc.dump(window='-1')
try:
#	vc.findViewByIdOrRaise("com.antutu.ABenchMar:id/negative_btn")
	attention_ok_button = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/negative_btn")
	attention_ok_button.touch()
	print ("Pass the Attention Error..")
except:
#	print "No Attention error"
	pass
"""

#Start test button
vc.dump(window='-1')
start_button = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/test_btn")
start_button.touch()
print ("Test_Btn")

#Start all test button
vc.dump(window='-1')
start_test_button = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/start_test_text")
start_test_button.touch()
print ("Start_test_text")

#Wait while antutu5 is running benchmark

finished = False
time.sleep(240)

while(not finished):
	time.sleep(3)
	vc.dump(window='-1')
	try:
#		progress_button = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/total_score_layout")
		progress_button = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/main_chart_layout")
		finished = True
	except ViewNotFoundException:
		pass

print ("Benchmark Finished")
time.sleep(2)
detail_button = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/detail_btn")
detail_button.touch()
print("detail_btn")

# psw0523 add for portrait mode
get_results_done = False
while get_results_done == False:
    try:
        call(['adb', 'shell', 'settings', 'put', 'system', 'user_rotation', '1'])
        #Get the score
        vc.dump(window='-1')
        multitask_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/ue_multitask_text")
        runtime_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/ue_dalvik_text")
        ram_operation_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/mem_text")
        ram_speed_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/ram_text")
        cpu_clock = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/cpu_attr_text")
        cpu_multi_integer_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/cpu_int_text")
        cpu_multi_float_point_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/cpu_float_text")
        cpu_single_integer_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/cpu_int_text2")
        cpu_single_float_point_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/cpu_float_text2")
        twod_graphics_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/gpu_2d_text")
        threed_graphics_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/gpu_3d_text")
        storage_io_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/io_sdw_text")
        database_io_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/io_db_text")
        get_results_done = True
    except:
        print("exception occurred --> Retry...")

# psw0523 debugging
print(['lava-test-case', '"AnTuTu 5.0 Alpha UX Multitask Score"', '--result', 'pass', '--measurement', multitask_score.getText()])
print(['lava-test-case', '"AnTuTu 5.0 Alpha UX Runtime Score"', '--result', 'pass', '--measurement', runtime_score.getText()])
print(['lava-test-case', '"AnTuTu 5.0 Alpha RAM Operation Score"', '--result', 'pass', '--measurement', ram_operation_score.getText()])
print(['lava-test-case', '"AnTuTu 5.0 Alpha RAM Speed Score"', '--result', 'pass', '--measurement', ram_speed_score.getText()])
print(['lava-test-case', '"AnTuTu 5.0 Alpha Multi Core CPU Integer Score"', '--result', 'pass', '--measurement', cpu_multi_integer_score.getText()])
print(['lava-test-case', '"AnTuTu 5.0 Alpha Multi Core CPU Float-Point Score"', '--result', 'pass', '--measurement', cpu_multi_float_point_score.getText()])
print(['lava-test-case', '"AnTuTu 5.0 Alpha Single Thread CPU Integer Score"', '--result', 'pass', '--measurement', cpu_single_integer_score.getText()])
print(['lava-test-case', '"AnTuTu 5.0 Alpha Single Thread CPU Float-Point Score"', '--result', 'pass', '--measurement', cpu_single_float_point_score.getText()])
print(['lava-test-case', '"AnTuTu 5.0 Alpha GPU 2D Graphics Score"', '--result', 'pass', '--measurement', twod_graphics_score.getText()])
print(['lava-test-case', '"AnTuTu 5.0 Alpha GPU 3D Graphics Score"', '--result', 'pass', '--measurement', threed_graphics_score.getText()])
print(['lava-test-case', '"AnTuTu 5.0 Alpha IO Storage I/O Score"', '--result', 'pass', '--measurement', storage_io_score.getText()])
print(['lava-test-case', '"AnTuTu 5.0 Alpha IO Database I/O Score"', '--result', 'pass', '--measurement', database_io_score.getText()])

# this is org
call(['lava-test-case', 'AnTuTu 5.0 Alpha UX Multitask Score', '--result', 'pass', '--measurement', multitask_score.getText()])
call(['lava-test-case', 'AnTuTu 5.0 Alpha UX Runtime Score', '--result', 'pass', '--measurement', runtime_score.getText()])
call(['lava-test-case', 'AnTuTu 5.0 Alpha RAM Operation Score', '--result', 'pass', '--measurement', ram_operation_score.getText()])
call(['lava-test-case', 'AnTuTu 5.0 Alpha RAM Speed Score', '--result', 'pass', '--measurement', ram_speed_score.getText()])
call(['lava-test-case', 'AnTuTu 5.0 Alpha Multi Core CPU Integer Score', '--result', 'pass', '--measurement', cpu_multi_integer_score.getText()])
call(['lava-test-case', 'AnTuTu 5.0 Alpha Multi Core CPU Float-Point Score', '--result', 'pass', '--measurement', cpu_multi_float_point_score.getText()])
call(['lava-test-case', 'AnTuTu 5.0 Alpha Single Thread CPU Integer Score', '--result', 'pass', '--measurement', cpu_single_integer_score.getText()])
call(['lava-test-case', 'AnTuTu 5.0 Alpha Single Thread CPU Float-Point Score', '--result', 'pass', '--measurement', cpu_single_float_point_score.getText()])
call(['lava-test-case', 'AnTuTu 5.0 Alpha GPU 2D Graphics Score', '--result', 'pass', '--measurement', twod_graphics_score.getText()])
call(['lava-test-case', 'AnTuTu 5.0 Alpha GPU 3D Graphics Score', '--result', 'pass', '--measurement', threed_graphics_score.getText()])
call(['lava-test-case', 'AnTuTu 5.0 Alpha IO Storage I/O Score', '--result', 'pass', '--measurement', storage_io_score.getText()])
call(['lava-test-case', 'AnTuTu 5.0 Alpha IO Database I/O Score', '--result', 'pass', '--measurement', database_io_score.getText()])

'''
time.sleep(3)
menu_back_icon = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/menu_back_img")
menu_back_icon.touch()
print("Menu Back Icon1")
'''
'''
time.sleep(3)
menu_back_icon = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/menu_back_img")
menu_back_icon.touch()
print("Menu Back Icon2")
'''
