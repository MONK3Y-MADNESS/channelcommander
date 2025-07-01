import threading
import time
from devicemanager import DeviceManager

def main():
    manner = DeviceManager()
    streamdocks = manner.enumerate()

    if not streamdocks:
        print("No StreamDock devices found.")
        return

    for device in streamdocks:
        try:
            device.open()
            print(f"Opened device at {device.getPath()}")
        except Exception as e:
            print(f"Failed to open device: {e}")
            continue

        t = threading.Thread(target=device.whileread, daemon=True)
        t.start()

        device.set_brightness(100)
        device.set_touchscreen_image("images/1.jpg")
        time.sleep(1)
        device.set_key_image("images/2.jpg", 3)
        time.sleep(1)
        device.cleaerIcon(3)
        time.sleep(1)
        device.clearAllIcon()
        device.refresh()
        time.sleep(1)
        device.close()
        time.sleep(1)

if __name__ == "__main__":
    main()
