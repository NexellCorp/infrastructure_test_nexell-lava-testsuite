import re
import sys
import os
import time
from subprocess import call

from com.dtmilano.android.viewclient import ViewClient, ViewNotFoundException

device, serialno = ViewClient.connectToDeviceOrExit()
vc = ViewClient(device, serialno)

#Wait while application loads
time.sleep(2)

#Start test button
vc.dump(window='-1')
btn_classic = vc.findViewByIdOrRaise("com.into.stability:id/button1")
btn_classic.touch()
print ("Start Stability Test")
#Wait 
time.sleep(30)

print ("Start Stability Finished")

adsf

"""
time.sleep(2)
detail_button = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/detail_btn")
detail_button.touch()
print("detail_btn")

#Get the score
vc.dump(window='-1')
multitask_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/ue_multitask_text")
runtime_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/ue_dalvik_text")
ram_operation_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/mem_text")
ram_speed_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/ram_text")
cpu_multi_integer_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/cpu_int_text")
cpu_multi_float_point_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/cpu_float_text")
cpu_single_integer_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/cpu_int_text2")
cpu_single_float_point_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/cpu_float_text2")
twod_graphics_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/gpu_2d_text")
threed_graphics_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/gpu_3d_text")
storage_io_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/io_sdw_text")
database_io_score = vc.findViewByIdOrRaise("com.antutu.ABenchMark:id/io_db_text")

call(['lava-test-case', '"AnTuTu 5.0 Alpha UX Multitask Score"', '--result', 'pass', '--measurement', multitask_score.getText()])
call(['lava-test-case', '"AnTuTu 5.0 Alpha UX Runtime Score"', '--result', 'pass', '--measurement', runtime_score.getText()])
call(['lava-test-case', '"AnTuTu 5.0 Alpha RAM Operation Score"', '--result', 'pass', '--measurement', ram_operation_score.getText()])
call(['lava-test-case', '"AnTuTu 5.0 Alpha RAM Speed Score"', '--result', 'pass', '--measurement', ram_speed_score.getText()])
call(['lava-test-case', '"AnTuTu 5.0 Alpha Multi Core CPU Integer Score"', '--result', 'pass', '--measurement', cpu_multi_integer_score.getText()])
call(['lava-test-case', '"AnTuTu 5.0 Alpha Multi Core CPU Float-Point Score"', '--result', 'pass', '--measurement', cpu_multi_float_point_score.getText()])
call(['lava-test-case', '"AnTuTu 5.0 Alpha Single Thread CPU Integer Score"', '--result', 'pass', '--measurement', cpu_single_integer_score.getText()])
call(['lava-test-case', '"AnTuTu 5.0 Alpha Single Thread CPU Float-Point Score"', '--result', 'pass', '--measurement', cpu_single_float_point_score.getText()])
call(['lava-test-case', '"AnTuTu 5.0 Alpha GPU 2D Graphics Score"', '--result', 'pass', '--measurement', twod_graphics_score.getText()])
call(['lava-test-case', '"AnTuTu 5.0 Alpha GPU 3D Graphics Score"', '--result', 'pass', '--measurement', threed_graphics_score.getText()])
call(['lava-test-case', '"AnTuTu 5.0 Alpha IO Storage I/O Score"', '--result', 'pass', '--measurement', storage_io_score.getText()])
call(['lava-test-case', '"AnTuTu 5.0 Alpha IO Database I/O Score"', '--result', 'pass', '--measurement', database_io_score.getText()])
"""
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