#!/bin/bash

#need to be defined for different benchmark apks
activity="com.antutu.ABenchMark/.ABenchMarkStart"
apk_file_name="antutu-benchmark-v5-alpha.apk"
test_method="python vc_antutu5.py"
apk_package="com.antutu.ABenchMark"

#following should no need to modify
parent_dir=`dirname ${0}`
source "${parent_dir}/../common/common.sh"
main "$@"

