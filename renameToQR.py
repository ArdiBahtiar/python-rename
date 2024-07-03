from PIL import Image
from pyzbar.pyzbar import decode
import os
from pathlib import Path

path = "ADV"
index_list = os.listdir(path)

awal = int(input("Ubah mulai dari Index ke berapa?"))
akhir = int(input("Sampe Index ke berapa?"))

for x in range(awal, akhir):
    basename = os.path.basename(index_list[x])
    basename_path = Path(basename).stem
    img_path = os.path.join(path, f"{basename_path}.png")
    img_png = Image.open(img_path)
    
    # Decode the QR code
    decoded_objs = decode(img_png)
    
    if decoded_objs:
        qr_value = decoded_objs[0].data.decode("utf-8")  # Get the QR code value
        rgb_img = img_png.convert('RGB')
        output_path = os.path.join("QR-result", f"{qr_value}.jpg")
        rgb_img.save(output_path)
        print(f"Saved {output_path}")
    else:
        print(f"No QR code found in {img_path}")
