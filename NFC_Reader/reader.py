import RPi.GPIO as GPIO
import urllib.request
import time

from pn532 import *


# list of uids that have booking permission
allowed_uids = [
    ['0x4', '0x26', '0x5b', '0xca', '0x83', '0x64', '0x81']
    ]


if __name__ == "__main__":
    try:
        pn532 = PN532_UART(debug=False, reset=20)

        ic, ver, rev, support = pn532.get_firmware_version()
        print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))

        print("Waiting for access card...")
        while True:
            uid = pn532.read_passive_target(timeout=0.5)
            print('Waiting...\n', end="")
            if uid is None:
                continue
            found_uid = [hex(i) for i in uid]
            print("Found card with UID:", found_uid)
            if found_uid in allowed_uids:
                print(">Has booking permission - trying to book room ...")
                url = f"http://127.0.0.1:5000/bycard/{''.join(found_uid)}"
                if urllib.request.urlopen(url).read().decode("utf-8") == "True":
                    print("Room booked by card successfully!")
                else:
                    print("Error: Room was not booked. Room is probably already occupied!")
            else:
                print(">No booking permission!")
            cooldown = 5
            # start reading cooldown
            for seconds in reversed(range(cooldown)):
                print(f"Will resume reading in {seconds+1} ...")
                time.sleep(1)
        print(e)
    finally:
        GPIO.cleanup()
