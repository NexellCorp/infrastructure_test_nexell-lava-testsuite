#!/bin/bash
# Author: Benjamin Lim <benjamin@nexell.co.kr>

TARGET_DIR=/storage/sdcard0/DCIM/Camera

echo
echo "Delete a before result files"
#echo "Target DIR :"$TARGET_DIR

function del_result(){
	adb shell "rm -r $TARGET_DIR/*.*"

	if [ $? -ne 0 ]; then
		echo "Old test files delete failed!"
		echo
		return 1
	else
		echo "Old test files delete finished!"
		echo
		return 0
	fi
}


del_result
