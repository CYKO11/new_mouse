# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.ads1x15 import Mode
from adafruit_ads1x15.analog_in import AnalogIn

class A2DC:
    def __init__(self):
        # initiate i2c bus
        i2c = busio.I2C(board.SCL, board.SDA, frequency=1000000)

        # adafruit board config
        self.ads = ADS.ADS1115(i2c)
        self.ads.mode = Mode.CONTINUOUS
        self.ads.data_rate = 860
        self.sample_interval = 1.0 / self.ads.data_rate

        # setup readable channels
        self.chan0 = AnalogIn(self.ads, ADS.P0)
        self.chan1 = AnalogIn(self.ads, ADS.P1)
        self.chan2 = AnalogIn(self.ads, ADS.P2)
        self.chan3 = AnalogIn(self.ads, ADS.P3)

    def readSampleSet(self, sampleSize):
        _ = self.chan0.voltage
        _ = self.chan1.voltage
        _ = self.chan2.voltage
        _ = self.chan3.voltage
        
        data_chan0 = [None] * sampleSize
        data_chan1 = [None] * sampleSize
        data_chan2 = [None] * sampleSize
        data_chan3 = [None] * sampleSize

        time_next_sample = time.monotonic() + self.sample_interval

        # Read the same channel over and over
        for i in range(sampleSize):
            # Wait for expected conversion finish time
            while time.monotonic() < (time_next_sample):
                pass

            # Read conversion value for ADC channel
            data_chan0[i] = self.chan0.voltage
            data_chan1[i] = self.chan1.voltage
            data_chan2[i] = self.chan2.voltage
            data_chan3[i] = self.chan3.voltage
            time_next_sample = time.monotonic() + self.sample_interval

        return [data_chan0, data_chan1, data_chan2, data_chan3]
        # return data_chan3
