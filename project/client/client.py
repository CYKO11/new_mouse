import socket
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.ads1x15 import Mode
from adafruit_ads1x15.analog_in import AnalogIn

host = "192.168.8.100"  # as both code is running on same pc
port = 5000  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

# Data collection setup
RATE = 860
SAMPLES = 20

# Create the I2C bus with a fast frequency
# NOTE: Your device may not respect the frequency setting
#       Raspberry Pis must change this in /boot/config.txt

i2c = busio.I2C(board.SCL, board.SDA, frequency=1000000)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)

# ADC Configuration
ads.mode = Mode.CONTINUOUS
ads.data_rate = RATE

# First ADC channel read in continuous mode configures device
# and waits 2 conversion cycles
_ = chan0.value

def getData():
    sample_interval = 1.0 / ads.data_rate

    repeats = 0
    skips = 0

    data = [None] * SAMPLES

    start = time.monotonic()
    time_next_sample = start + sample_interval

    # Read the same channel over and over
    for i in range(SAMPLES):
        # Wait for expected conversion finish time
        while time.monotonic() < (time_next_sample):
            pass

        # Read conversion value for ADC channel
        data[i] = chan0.voltage

        # Loop timing
        time_last_sample = time.monotonic()
        time_next_sample = time_next_sample + sample_interval
        if time_last_sample > (time_next_sample + sample_interval):
            skips += 1
            time_next_sample = time.monotonic() + sample_interval

        # Detect repeated values due to over polling
        if data[i] == data[i - 1]:
            repeats += 1

    # client_socket.send(data.tostring().encode())
    message = "";
    for i in data:
        message += "\n" + str(i)

    client_socket.send(message.encode())

while True:
    getData()
    time.sleep(0.01)

client_socket.close()  # close the connection