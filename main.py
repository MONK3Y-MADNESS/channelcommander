from devicemanager import DeviceManager
import threading
import time

def main():
    manner = DeviceManager()

    # Start the device manager's listener thread
    listener_thread = threading.Thread(target=manner.listen, daemon=True)
    listener_thread.start()

    # Discover connected devices
    streamdocks = manner.enumerate()
    print("Found {} Stream Dock(s).\n".format(len(streamdocks)))

    # Track per-device whileread threads
    read_threads = []

    for device in streamdocks:
        device.open()
        device.refresh()

        # Start a thread to continuously read input from device
        t = threading.Thread(target=device.whileread, daemon=True)
        t.start()
        read_threads.append(t)

        # Perform operations
        device.set_brightness(100)
        device.set_touchscreen_image("1.jpg")
        time.sleep(1)
        device.set_key_image("2.jpg", 3)
        time.sleep(1)
        device.cleaerIcon(3)
        time.sleep(1)
        device.clearAllIcon()
        device.refresh()
        time.sleep(1)
        device.close()
        time.sleep(1)

    # Optional: join threads if you need to keep program alive, or skip if using daemon=True
    for t in read_threads:
        t.join()

    listener_thread.join()

if __name__ == "__main__":
    main()
