import os
from pyzbar.pyzbar import decode
from PIL import Image


image_folder = "C:/Users/Ttawi/Desktop/QRRR!/extracted_frames"  


def decode_qr_from_image(image_path):
    image = Image.open(image_path)
    decoded_objects = decode(image)
    return [obj.data.decode('utf-8') for obj in decoded_objects]


for image_filename in os.listdir(image_folder):
    if image_filename.endswith(".png"):  # تأكد من أن الصور بصيغة PNG
        image_path = os.path.join(image_folder, image_filename)
        decoded_data = decode_qr_from_image(image_path)
        if decoded_data:
            print(f"الكود في {image_filename}: {decoded_data}")
        else:
            print(f"لم يتم العثور على QR في {image_filename}")
