from mfrc522 import MFRC522
from time import sleep

reader = MFRC522(
    sck=2,
    mosi=3,
    miso=4,
    rst=6,
    cs=5
)

print("RFID reader started")

while True:
    status, tag_type = reader.request(reader.REQIDL)

    if status == reader.OK:
        print("Card detected!")

        status, uid = reader.anticoll()

        if status == reader.OK:
            print("UID:", uid)
        else:
            print("Could not read UID")

    sleep(0.5)