import hid

class HIDTransport:
    def __init__(self, path):
        self.path = path
        self.device = hid.device()

    def open(self):
        self.device.open_path(self.path.encode())
        print(f"Connected to {self.path}")

    def disconnected(self):
        self.device.close()

    def keyClear(self, index):
        print(f"Clearing icon on key {index}")

    def keyAllClear(self):
        print("Clearing all icons")

    def wakeScreen(self):
        print("Waking screen")

    def refresh(self):
        print("Refreshing display")

    def read(self):
        return self.device.read(512)

    @staticmethod
    def enumerate_devices():
        devices = hid.enumerate()
        return [d['path'] for d in devices if d['vendor_id'] == 0x0300 and d['product_id'] == 0x3004]
