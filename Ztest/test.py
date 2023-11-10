from dataclasses import dataclass
from Tools import loggingTools
import logging

import pyvisa


@dataclass
class DCPower2:
    def __init__(self):
        # self.addr: str = "TCPIP0::192.168.1.40::inst0::INSTR"
        # self.name: str = 'DC Power2'
        # self.idn: str = 'ITECH Electronics,IT2805,805483011787110017,000.001.053-0.14-1.08-0.70'

        self.addr: str = 'USB0::0x2EC7::0x6700::802260084767510008::INSTR'
        self.idn: str = 'ITECH Ltd., IT6722, 802260084767510008,  1.17-1.04'
        self.name: str = 'DC_Power2'
        self.resource = None

    def connect(self):
        try:
            self.resource = pyvisa.ResourceManager().open_resource(self.addr, timeout=500)
            logging.info("{} is connecting...".format(self.name))
            return True
        except pyvisa.VisaIOError as ex:
            logging.info(ex)
            logging.info("{} is disconnect...".format(self.name))
            return False

    def disconnect(self):
        try:
            if self.resource:
                self.resource.close()
                logging.info("{} is closed...".format(self.name))
        except Exception as ex:
            logging.info(ex)
            logging.info("{} can't close ...".format(self.name))

    def isExist(self):
        try:
            pyvisa.ResourceManager().open_resource(self.addr, timeout=500)
            logging.info(" {} is exists!".format(self.name))
            return True
        except pyvisa.VisaIOError as ex:
            logging.info(ex)
            logging.info("{} is not exists...".format(self.name))
            return False

    def write(self, msg):
        try:
            if not self.resource:
                self.connect()
            self.resource.write(msg)
            logging.info("{} receive : '{}'".format(self.name,msg))
        except Exception as ex:
            logging.info(ex)
            logging.info("{} can't write to...".format(self.name))

    def query(self, msg):
        try:
            if not self.resource:
                self.connect()
            response = self.resource.query(msg).strip()
            logging.info("{} receive : '{}'".format(self.name,msg))
            return response
        except Exception as ex:
            logging.info(ex)
            logging.info("{} can't query to...".format(self.name))

    def deviceInfo(self):
        return self.idn

    def __del__(self):
        self.disconnect()

    def __repr__(self):
        return self.idn


if __name__ == "__main__":
    dc_power = DCPower2()
    # if dc_power.isExist():
    print(dc_power.query('*idn?'))
