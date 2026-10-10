from machine import Pin
from time import sleep
from mfrc522 import MFRC522

reader = MFRC522(
    sck=2,
    mosi=3,
    miso=4,
    rst=6,
    cs=5
)

green_led = Pin(14, Pin.OUT)
red_led = Pin(16, Pin.OUT)

buzzer = Pin(15, Pin.OUT)
buzzer.value(1)  

green_led.value(0)
red_led.value(0)

AUTHORIZED_UIDS = [
    [119, 106, 193, 62, 226]
]

print("RFID Access Control Ready")

while True:
    status, tag_type = reader.request(reader.REQIDL)

    if status == reader.OK:
        status, uid = reader.anticoll()

        if status == reader.OK:
            print("Card UID:", uid)

            if uid in AUTHORIZED_UIDS:
                print("ACCESS GRANTED")

                green_led.value(1)
                red_led.value(0)

                buzzer.value(0)
                sleep(0.15)
                buzzer.value(1)

            else:
                print("ACCESS DENIED")

                green_led.value(0)
                red_led.value(1)

                for _ in range(2):
                    buzzer.value(0)
                    sleep(0.12)
                    buzzer.value(1)
                    sleep(0.12)

            
            sleep(1)
            green_led.value(0)
            red_led.value(0)

        sleep(0.5)

    sleep(0.1)

