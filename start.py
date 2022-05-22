from subprocess import Popen, PIPE
import subprocess
import os
import time

dirname = os.path.dirname(__file__)

webserver_path = os.path.join(dirname, "Website/main.py")
display_path = os.path.join(dirname, "Display/display.py")
nfc_reader_path = os.path.join(dirname, "NFC_Reader/reader.py")

webserver_process = Popen(["lxterminal", "-e", "python3", "-i", webserver_path])
time.sleep(5) # wait for webserver to fully start
webserver_process = Popen(["lxterminal", "-e", "python3", "-i", display_path])
nfc_process = Popen(["lxterminal", "-e", "python3", "-i", nfc_reader_path])

