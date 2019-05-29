import usb.core
# use venv

# dev = usb.core.find()

dev = usb.core.show_devices()

print(dev)
# DEVICE ID 05ac:0250
# 05ac is Vendor ID, 0250 is product id

# On Mac OS to get usb devices: system_profiler SPUSBDataType
