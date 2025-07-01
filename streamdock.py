from abc import ABC, abstractmethod
from transport.hidtransport import HIDTransport

class StreamDock(ABC):
    def __init__(self, path):
        self.path = path
        self.transport = HIDTransport(path)

    def open(self):
        self.transport.open()

    def close(self):
        self.disconnected()

    def disconnected(self):
        self.transport.disconnected()

    def cleaerIcon(self, index):
        self.transport.keyClear(index)

    def clearAllIcon(self):
        self.transport.keyAllClear()

    def wakeScreen(self):
        self.transport.wakeScreen()

    def refresh(self):
        self.transport.refresh()

    def getPath(self):
        return self.path

    def read(self):
        return self.transport.read()

    def whileread(self):
        while True:
            arr = self.read()
            if len(arr) >= 10:
                if arr[9] == 0xFF:
                    print("Write Success")
                else:
                    print(f"Button {arr[9]}")
                    print("Pressed" if arr[10] == 0x01 else "Up")
            else:
                print(arr)

    @abstractmethod
    def get_serial_number(self):
        pass

    @abstractmethod
    def set_key_image(self, key, image):
        pass

    @abstractmethod
    def set_brightness(self, percent):
        pass

    @abstractmethod
    def set_touchscreen_image(self, image):
        pass

    @abstractmethod
    def set_key_imagedata(self, key, image, width=126, height=126):
        pass
