#!/usr/bin/python

import logging
import math
import time
from Adafruit_I2C import Adafruit_I2C

# HTU21D Address
HTU21DF_I2CADDR =  0x40
HTU21DF_READTEMP = 0xE3
HTU21DF_READHUM = 0xE5
HTU21DF_WRITEREG = 0xE6
HTU21DF_READREG = 0xE7
HTU21DF_RESET = 0xFE



class HTU21D(object):
    "Class to represent an Adafruit MCP9808 precision temperature measurement board."
    def __init__(self, address=HTU21D_I2CADDR, i2c=None, debug=False):
        if i2c is None:
            import Adafruit_I2C as I2C
            i2c = I2C
        self.address = address
    def reset():
        pause
    def readTemperature(self):
        self.i2c.write16(self,HTU21DF_READTEMP,0)
        self.i2c.readU16(self,HTU21DF_READTEMP,0)

#        // OK lets ready!
#        Wire.beginTransmission(HTU21DF_I2CADDR);
#        Wire.write(HTU21DF_READTEMP);
#        Wire.endTransmission();
#
#        delay(50); // add delay between request and actual read!
#
#        Wire.requestFrom(HTU21DF_I2CADDR, 3);
#        while (!Wire.available()) {}
#
#        uint16_t t = Wire.read();
#        t <<= 8;
#        t |= Wire.read();
#
#        uint8_t crc = Wire.read();
#
#        float temp = t;
#        temp *= 175.72;
#        temp /= 65536;
#        temp -= 46.85;
#
#        return temp;
#        }


H = HTU21D()
