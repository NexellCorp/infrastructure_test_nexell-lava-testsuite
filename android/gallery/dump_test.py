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

#Start test button
vc.dump('-1')
test_btn = vc.findViewByIdOrRaise("android:id/action_bar_spinner")
test_btn.touch()