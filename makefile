ARDUINO_DIR = /usr/share/arduino
TEENSYDUINO_DIR = /usr/local/teensy
BOARD = teensy41
MCU = IMXRT1062
HEXFILE = main.ino.hex
PORT = /dev/ttyACM0  # Vérifie avec `ls /dev/tty*`

compile:
	arduino-cli compile --fqbn teensy:avr:$(BOARD) --output-dir build CodeArduino/CodeArduino.ino

upload:
	teensy-loader-cli --mcu=$(MCU) -w -v build/CodeArduino.ino.hex

all: compile upload
