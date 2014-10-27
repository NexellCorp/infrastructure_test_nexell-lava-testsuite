#!/bin/bash

# need to be defined for different benchmark apks
activity="com.into.stability/.Run"
apk_file_name="stabilitytest-root-optional-2.7.apk"

# The first added parameter has been reserved by Android View Client.
# In order to add customised parameter, the first one must be the serial number from ADB
if [ -z "$1" ]; then
    device_serial_number=`adb get-serialno`
else
    device_serial_number=$1
fi

test_method="python vc_stability.py $device_serial_number $excluded_test_suite"
apk_package="com.into.stability"

# following should no need to modify
parent_dir=`dirname ${0}`
source "${parent_dir}/../common/common.sh"
timeout=30m
main "$@"

