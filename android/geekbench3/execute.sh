#!/bin/bash

# need to be defined for different benchmark apks
activity="com.primatelabs.geekbench/.HomeActivity"
apk_file_name="com.primatelabs.geekbench.apk"

# The first added parameter has been reserved by Android View Client.
# In order to add customised parameter, the first one must be the serial number from ADB
if [ -z "$1" ]; then
    device_serial_number=`adb get-serialno`
else
    device_serial_number=$1
fi

test_method="python vc_geekbench3.py $device_serial_number $excluded_test_suite"
apk_package="com.primatelabs.geekbench"

# following should no need to modify
parent_dir=`dirname ${0}`
source "${parent_dir}/../common/common.sh"
timeout=30m
main "$@"
