from ajazz_akp05 import AJAZZ_AKP05
from transport.hidtransport import HIDTransport

class DeviceManager:
    def __init__(self):
        self.devices = []

    def enumerate(self):
        # Find connected HID devices
        paths = HIDTransport.enumerate_devices()

        for path in paths:
            # For now, assume everything is an AJAZZ_AKP05 — 
            # you can improve this by checking VID/PID later.
            device = AJAZZ_AKP05(path)
            self.devices.append(device)

        return self.devices

    def listen(self):
        while True:
            for device in self.devices:
                device.refresh()
