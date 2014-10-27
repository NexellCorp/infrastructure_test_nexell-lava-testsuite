#!/bin/bash

#need to be defined for different benchmark apks
activity="com.glbenchmark.glbenchmark27/net.kishonti.gfxbench.GfxMainActivity"
apk_file_name="com.glbenchmark.glbenchmark27.apk"
test_method="python vc_GFXBench3.py"
apk_package="com.glbenchmark.glbenchmark27"

#following should no need to modify
parent_dir=`dirname ${0}`
source "${parent_dir}/../common/common.sh"
main "$@"
