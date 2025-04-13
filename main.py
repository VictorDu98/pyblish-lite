import sys
sys.path.append(r"D:\tools\pyblish-lite")
# 1. Register your favourite GUI
import pyblish.api
import pyblish_lite
import pyblish.util

pyblish.api.register_host("maya")
pyblish.api.register_plugin_path(r"D:\tools\pyblish-lite\Collect")
pyblish.util.publish()
window = pyblish_lite.show()