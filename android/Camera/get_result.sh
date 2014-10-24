#!/bin/bash
# Author: Botao Sun <botao.sun@linaro.org>

RESULT_DIR=Camera_result
TARGET_DIR=/storage/sdcard0/DCIM/Camera

function get_result(){
    echo "Camera test result transfer in progress..."
	echo "Target DIR :"$1 ", Dest DIR :"$2
    adb pull $1 $2
#    adb shell "rm -r /storage/sdcard0/DMIC/Camera/*.*"
    if [ $? -ne 0 ]; then
        echo "Test result transfer failed!"
        return 1
    else
        echo "Test result transfer finished!"
        # Rename the file, should be only one .gb3 file on target directory
#       mv *.gb3 geekbench3_result.gb3
#        if [ $? -ne 0 ]; then
#            echo "File rename failed! There should be only one .gb3 file under the current directory!"
#            return 1
#        else
#            echo "Test result file for Geekbench 3 now is geekbench3_result.gb3"
            return 0
#        fi
    fi
}

mkdir -p Camera_result
get_result $TARGET_DIR $RESULT_DIR
#get_result "/storage/sdcard0/DMIC/Camera", "Camera_result"
