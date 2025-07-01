from devicemanager import DeviceManager
import threading
import time
import os

DEBUG = True  # Set to False to silence debug output

def debug_print(msg):
    if DEBUG:
        print(msg)

def main():
    manner = DeviceManager()

    debug_print("Starting device manager listener thread...")
    listener_thread = threading.Thread(target=manner.listen, daemon=True)
    listener_thread.start()

    debug_print("Enumerating connected Stream Dock devices...")
    streamdocks = manner.enumerate()
    debug_print(f"Found {len(streamdocks)} Stream Dock(s).\n")

    read_threads = []

    # Base path for images
    image_folder = os.path.join(os.path.dirname(__file__), "images")

    for device in streamdocks:
        debug_print(f"Opening device: {device.getPath()}")
        device.open()
        device.refresh()

        t = threading.Thread(target=device.whileread, daemon=True)
        t.start()
        read_threads.append(t)

        device.set_brightness(100)
        debug_print("Set brightness to 100")

        touchscreen_img = os.path.join(image_folder, "Action-Icon.png")
        debug_print(f"Setting touchscreen image: {touchscreen_img}")
        device.set_touchscreen_image(touchscreen_img)
        time.sleep(1)

        key_image = os.path.join(image_folder, "Key&Plugin-Icon.png")
        debug_print(f"Setting key image on key 3: {key_image}")
        device.set_key_image(key_image, 3)
        time.sleep(1)

        debug_print("Clearing icon on key 3")
        device.cleaerIcon(3)
        time.sleep(1)

        category_image = os.path.join(image_folder, "Category-Icon.png")
        debug_print(f"Setting key image on key 4: {category_image}")
        device.set_key_image(category_image, 4)
        time.sleep(1)

        debug_print("Clearing all icons")
        device.clearAllIcon()
        device.refresh()
        time.sleep(1)

        debug_print(f"Closing device: {device.getPath()}")
        device.close()
        time.sleep(1)

    debug_print("All devices processed. Keeping program alive. Press Ctrl+C to exit.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        debug_print("Exiting program...")

if __name__ == "__main__":
    main()
