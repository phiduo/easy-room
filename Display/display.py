import time
import datetime
import urllib.request
import requests
import os
from demo_opts import get_device
from luma.core.render import canvas
from pathlib import Path
from PIL import ImageFont

# configured display fonts
#font_path = "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"
font_path = "LiberationSans-Regular.ttf"
font_upper = ImageFont.truetype(font_path, 30)
font_lower = ImageFont.truetype(font_path, 17)
font_occupied = ImageFont.truetype(font_path, 35)


def main():
    device = get_device()
    while True:
        url = "http://127.0.0.1:5000/isAvailable"
        resp = requests.get(url)
        data = resp.json()  
        if data["isAvailable"] == "True":
            displayed_av = "Frei"
            displayed_time = "30+ Minuten" if data["minutes"] > 30 else f"{data['minutes']} Minuten"      
        else:
            displayed_av = "Besetzt"
        # show availability on display
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            if data["isAvailable"] == "True": 
                draw.text((6,6), str(displayed_av), font=font_upper, fill="white")
                draw.text((7,35), f"für {displayed_time}", font=font_lower, fill="white")
            else:
                draw.text((6,10), str(displayed_av), font=font_occupied, fill="white")
        time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

