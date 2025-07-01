from streamdock import StreamDock
from transport.hidtransport import HIDTransport

class DeviceManager:
    def __init__(self):
        self.devices = []

    def enumerate(self):
        # Example: discover connected devices (simplified mockup)
        paths = HIDTransport.enumerate_devices()

        for path in paths:
            device = StreamDock(path)
            self.devices.append(device)

        return self.devices
