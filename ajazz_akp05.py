import os
import ctypes
from PIL import Image
from streamdock import StreamDock

class AJAZZ_AKP05(StreamDock):
    def set_brightness(self, percent):
        return self.transport.setBrightness(percent)

    def set_touchscreen_image(self, image_path):
        image = Image.open(image_path)
        image = image.convert('RGB')
        width, height = image.size
        pixels = list(image.getdata())
        bgr_data = []
        for pixel in pixels:
            r, g, b = pixel
            bgr_data.extend([r, g, b])
        arr_type = ctypes.c_char * len(bgr_data)
        arr_ctypes = arr_type(*bgr_data)
        reversed_bgr_array = arr_ctypes[::-1]
        return self.transport.setBackgroundImg(reversed_bgr_array, width * height * 3)

    def set_key_image(self, image_path, key):
        image1 = Image.open(image_path)
        rotated_image = image1.rotate(180)
        temp_image_path = "Temporary.jpg"
        rotated_image.save(temp_image_path)
        return_value = self.transport.setKeyImg(bytes(temp_image_path, 'utf-8'), key)
        os.remove(temp_image_path)
        return return_value

    def get_serial_number(self, length):
        return self.transport.getInputReport(length)

    def set_key_imagedata(self, key, image_data, width=126, height=126):
        # Assuming your transport layer supports this method:
        return self.transport.setKeyImgData(key, image_data, width, height)
