import dontpad
import sys

def error():
    print("Incorrect parameters.")
    print("Format:\n    dontpad [MODE] [URL_EXTENSION] [TEXT]")
    print("    MODES:\n    -r (default)\t\tRead content from URL_EXTENSION.\n    -w          \t\tWrite TEXT to URL_EXTENSION.")
    exit(-1)

argc = len(sys.argv)

if argc < 2:
    error()

if argc >= 3:
    url_extension = sys.argv[2]
    mode = "-r"
    mode = sys.argv[1]
    if mode == "-r":
        print(dontpad.read(url_extension))
    elif mode == "-w":
        text = " ".join(sys.argv[3:])
        dontpad.write(url_extension, text)
elif sys.argv[1] not in ["-r", "-w"]:
    url_extension = sys.argv[1]
    print(dontpad.read(url_extension))
else:
    error()

