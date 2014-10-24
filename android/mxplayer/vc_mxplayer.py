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

package_name = "com.mxtech.videoplayer.ad"


def screen_touch():
#	os.system("adb shell input touchscreen swipe 550 290 550 290 200")
	device.shell('input touchscreen swipe 550 290 550 290 200')


def screen_swipe_test():
	button = vc.findViewWithTextOrRaise('Show Dialog')
	print "button: ", button.getClass(), button.getId(), button.getCoords()
	
	
def chk_movie_folder():
	chk_movie_file = vc.findViewByIdOrRaise("android:id/empty")
	chk_movie_str = chk_movie_file.getText()
	print "1 :", chk_movie_file
	print "2 :", chk_movie_str
	print "3 :", chk_movie_file.find('empty')
	if(chk_movie_str.find('empty') != -1):
		print "No Video :", chk_movie_str
		sys.exit(1)
	
	btn_movie_folder = vc.findViewByIdOrRaise(package_name + ":id/name")
	btn_movie_str = btn_movie_folder.getText()
	print btn_movie_folder, btn_movie_str
	if(btn_movie_str.find('Movie') != -1):
		print "Found a Movie Folder from 1'st line"
		btn_movie_folder.touch()
		print "Enter the Movie folder"
		time.sleep(1)
		return

	id_movie_folder = vc.findViewByIdOrRaise("id/no_id/22")
	id_movie_str = id_movie_folder.getText()
	if(id_movie_str.find('Movie') != -1):
		print "Found a Movie Folder from 2'nd line"
		id_movie_folder.touch()
		print "Enter the Movie folder"
		time.sleep(1)
		return

	print "Unknown situation.. Please check the screen."
	print "No more test for MxPlayer.."
	sys.exit(1)


def chk_popup():
	chk_popup_win = vc.findViewByIdOrRaise(package_name + ":id/button1")
	if not chk_popup_win.isChecked():
		chk_popup_win.touch()
		print "Check a Resume", chk_popup_win.getCenter()
	else:
		print "No Pop-up Window"


def main():
	movie_cnt = 3
	
	vc.dump(window='-1')
	time.sleep(1)
#    if(btn_movie_folder = vc.findViewByIdOrRaise(package_name + ":id/name") != -1):
#	btn_movie_folder = vc.findViewByIdOrRaise(package_name + ":id/name")
	chk_movie_folder()


	vc.dump()
	time.sleep(1)
	tch_movie_file = vc.findViewByIdOrRaise(package_name + ":id/title")
	tch_movie_file.touch()
	print "Play a Movie file"
	
	time.sleep(1)
#	vc.dump()
#	chk_popup()
	

#	time.sleep(60*10)
#	time.sleep(1)
	
#	screen_touch()
#	screen_swipe_test()
	
	

if __name__ == '__main__':
    main()