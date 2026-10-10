# RFID Access Control System

A beginner-friendly electronics and programming project built to explore the fundamentals of embedded systems. Build using a Raspberry Pi Pico (RP2040), an MFRC522 RFID reader, LEDs, and a buzzer, this project introduces hardware wiring, MicroPython, and RFID communication through a simple access control system.

## Hardware

- Raspberry Pi Pico (RP2040)
- MFRC522 RFID reader module
- RFID card and key fob
- Two different colored LEDs 
- Two 220 Ω resistors (one per LED)
- Active buzzer module
- Breadboard and jumper wires
- USB cable for programming and power

## Pin Connections

### MFRC522 RFID Reader

| MFRC522 Pin | Pico GPIO / Pin |
|---|---|
| SCK | GP2 |
| MOSI | GP3 |
| MISO | GP4 |
| SDA / CS | GP5 |
| RST | GP6 |
| 3.3V | 3V3(OUT) |
| GND | GND |
| IRQ | Not connected |

### Indicators and Buzzer

| Component | Pico GPIO |
|---|---|
|  LED | GP14 |
| Active buzzer signal | GP15 |
|  LED | GP16 |

Each LED is connected in series with a 220 Ω resistor. The buzzer module uses an active-low signal, meaning it turns on when its control pin is set LOW.

## How It Works

1. The system initializes the RFID reader, LEDs, and buzzer.
2. An RFID card or key fob is presented to the reader.
3. The reader obtains the credential's UID.
4. The UID is compared against the authorized UID list.
5. If the UID is authorized:
   - One of the LEDs lights up
   - The buzzer produces one short beep.
   - The serial console displays `ACCESS GRANTED`.
6. If the UID is not authorized:
   - The other LED turns on.
   - The buzzer produces two short beeps.
   - The serial console displays `ACCESS DENIED`.
7. The indicator LEDs turn off after the feedback sequence.

## Software

- MicroPython
- Thonny IDE
- MFRC522 RFID driver

The program runs on the Pico and prints card UIDs and access decisions to the serial console.

## Setup

1. Install MicroPython on the Raspberry Pi Pico.
2. Copy the MFRC522 driver to the Pico.
3. Upload `main.py` and the required RFID driver file to the device.
4. Connect the hardware according to the pin tables above.
5. Add authorized card UIDs to the `AUTHORIZED_UIDS` list in `main.py`.
6. Run the program in Thonny and scan an RFID credential.

## Current Status

The current prototype successfully reads RFID credentials, checks authorization, controls two LED indicators, and provides buzzer feedback.

## Future Improvements

- Integrate a servo-operated physical latch.
- Store authorized credentials in a separate configuration file.
- Add a way to enroll or remove authorized credentials.
- Add event logging for access attempts.

## Security Limitations

This project is an educational prototype, not a production security system. Authorization currently relies on RFID UIDs, which be easily copied on some RFID technologies. UID-based checks alone should not be used to protect valuable property.
