import logging
import time
from dataclasses import dataclass

import pyvisa


@dataclass
class ACPower:
    def __init__(self):
        self.addr: str = "TCPIP0::192.168.1.30::hislip0::INSTR"
        self.name: str = 'AC Power'
        self.idn: str = 'KIKUSUI,PCR1000MA,DT003533, 2.01'
        self.timeout = 100
        self.resource = None

    def connect(self):
        try:
            self.resource = pyvisa.ResourceManager().open_resource(self.addr, open_timeout=self.timeout)
            logging.info("{} is connecting...".format(self.name))
            return True
        except pyvisa.VisaIOError as ex:
            logging.info("{} is disconnect...".format(self.name))
            logging.error(ex)
            return False

    def disconnect(self):
        try:
            if self.resource:
                self.resource.close()
                logging.info("{} is closed...".format(self.name))
        except Exception as ex:
            logging.info("{} can't close ...".format(self.name))
            logging.error(ex)

    def isExist(self):
        try:
            self.resource = pyvisa.ResourceManager().open_resource(self.addr, open_timeout=self.timeout)
            logging.info(" {} is exists!".format(self.name))
            return True
        except pyvisa.VisaIOError as ex:
            logging.info("{} is not exists...".format(self.name))
            logging.error(ex)
            return False

    def write(self, msg):
        try:
            if not self.resource:
                self.connect()
            self.resource.write(msg)
            logging.info("{} receive : '{}'".format(self.name, msg))
        except Exception as ex:
            logging.info("{} can't write to...".format(self.name))
            logging.error(ex)

    def query(self, msg):
        try:
            if not self.resource:
                self.connect()
            response = self.resource.query(msg).strip()
            logging.info("{} receive : '{}'".format(self.name, msg))
            return response
        except Exception as ex:
            logging.info("{} can't query to...".format(self.name))
            logging.error(ex)

    def deviceInfo(self):
        return self.idn

    # def __del__(self):
    #     self.disconnect()

    def __repr__(self):
        return self.idn


@dataclass
class DCPower1:

    def __init__(self):
        self.addr: str = "TCPIP0::192.168.1.10::hislip0::INSTR"
        self.name: str = 'DC Power1'
        self.idn: str = 'KIKUSUI,PWR801L,DS001499,VER01.25 BLD0057'
        self.timeout = 100
        self.resource = None

    def connect(self):
        try:
            self.resource = pyvisa.ResourceManager().open_resource(self.addr, open_timeout=self.timeout)
            logging.info("{} is connecting...".format(self.name))
            return True
        except pyvisa.VisaIOError as ex:
            logging.info("{} is disconnect...".format(self.name))
            logging.error(ex)
            return False

    def disconnect(self):
        try:
            if self.resource:
                self.resource.close()
                logging.info("{} is closed...".format(self.name))
        except Exception as ex:
            logging.info("{} can't close ...".format(self.name))
            logging.error(ex)

    def isExist(self):
        try:
            self.resource = pyvisa.ResourceManager().open_resource(self.addr, open_timeout=self.timeout)
            logging.info(" {} is exists!".format(self.name))
            return True
        except pyvisa.VisaIOError as ex:
            logging.info("{} is not exists...".format(self.name))
            logging.error(ex)
            return False

    def write(self, msg):
        try:
            if not self.resource:
                self.connect()
            self.resource.write(msg)
            logging.info("{} receive : '{}'".format(self.name, msg))
        except Exception as ex:

            logging.info("{} can't write to...".format(self.name))
            logging.error(ex)

    def query(self, msg):
        try:
            if not self.resource:
                self.connect()
            response = self.resource.query(msg).strip()
            logging.info("{} receive : '{}'".format(self.name, msg))
            return response
        except Exception as ex:

            logging.info("{} can't query to...".format(self.name))
            logging.error(ex)

    def deviceInfo(self):
        return self.idn

    # def __del__(self):
    #     self.disconnect()

    def __repr__(self):
        return self.idn


@dataclass
class DCPower2:
    def __init__(self):
        self.addr: str = "TCPIP0::192.168.1.40::inst0::INSTR"
        self.idn: str = 'ITECH Electronics,IT2805,805483011787110017,000.001.053-0.14-1.08-0.70'

        # self.addr: str = 'USB0::0x2EC7::0x6700::802260084767510008::INSTR'
        # self.idn: str = 'ITECH Ltd., IT6722, 802260084767510008,  1.17-1.04'
        self.name: str = 'DC_Power2'
        self.timeout = 100
        self.resource = None

    def connect(self):
        try:
            self.resource = pyvisa.ResourceManager().open_resource(self.addr, open_timeout=self.timeout)
            logging.info("{} is connecting...".format(self.name))
            return True
        except pyvisa.VisaIOError as ex:

            logging.info("{} is disconnect...".format(self.name))
            logging.error(ex)
            return False

    def disconnect(self):
        try:
            if self.resource:
                self.resource.close()
                logging.info("{} is closed...".format(self.name))
        except Exception as ex:
            logging.info("{} can't close ...".format(self.name))
            logging.error(ex)

    def isExist(self):
        try:
            self.resource = pyvisa.ResourceManager().open_resource(self.addr, open_timeout=self.timeout)
            logging.info(" {} is exists!".format(self.name))
            return True
        except pyvisa.VisaIOError as ex:

            logging.info("{} is not exists...".format(self.name))
            logging.error(ex)
            return False

    def write(self, msg):
        try:
            if not self.resource:
                self.connect()
            self.resource.write(msg)
            logging.info("{} receive : '{}'".format(self.name, msg))
        except Exception as ex:

            logging.info("{} can't write to...".format(self.name))
            logging.error(ex)

    def query(self, msg):
        try:
            if not self.resource:
                self.connect()
            response = self.resource.query(msg).strip()
            logging.info("{} receive : '{}'".format(self.name, msg))
            return response
        except Exception as ex:

            logging.info("{} can't query to...".format(self.name))
            logging.error(ex)

    def deviceInfo(self):
        return self.idn

    # def __del__(self):
    #     self.disconnect()

    def __repr__(self):
        return self.idn


@dataclass
class Multimeter:
    def __init__(self):
        self.addr: str = "TCPIP0::192.168.1.20::inst0::INSTR"
        self.name: str = 'Digtal Multimeter'
        self.idn: str = 'Rigol Technologies,DM3068,DM3O250700263,01.01.00.01.11.00'
        self.timeout = 100
        self.resource = None

    def connect(self):
        try:
            self.resource = pyvisa.ResourceManager().open_resource(self.addr, open_timeout=self.timeout)
            logging.info("{} is connecting...".format(self.name))
            return True
        except pyvisa.VisaIOError as ex:
            logging.info("{} is disconnect...".format(self.name))
            logging.error(ex)
            return False

    def disconnect(self):
        try:
            if self.resource:
                self.resource.close()
                logging.info("{} is closed...".format(self.name))
        except Exception as ex:
            logging.info("{} can't close ...".format(self.name))
            logging.error(ex)

    def isExist(self):
        try:
            self.resource = pyvisa.ResourceManager().open_resource(self.addr, open_timeout=self.timeout)
            logging.info(" {} is exists!".format(self.name))
            return True
        except pyvisa.VisaIOError as ex:
            logging.info("{} is not exists...".format(self.name))
            logging.error(ex)
            return False

    def write(self, msg):
        try:
            if not self.resource:
                self.connect()
            self.resource.write(msg)
            logging.info("{} receive : '{}'".format(self.name, msg))
        except Exception as ex:
            logging.info("{} can't write to...".format(self.name))
            logging.error(ex)
    def query(self, msg):
        try:
            if not self.resource:
                self.connect()
            response = self.resource.query(msg).strip()
            logging.info("{} receive : '{}'".format(self.name, msg))
            return response
        except Exception as ex:
            logging.info("{} can't query to...".format(self.name))
            logging.error(ex)

    def deviceInfo(self):
        return self.idn

    # def __del__(self):
    #     self.disconnect()

    def __repr__(self):
        return self.idn


@dataclass
class SignalGenerator:

    def __init__(self):
        self.addr: str = "USB0::0xF4ED::0xEE3A::SDG08CBD6R0561::INSTR"
        self.name: str = 'Signal Generator'
        self.idn: str = '*IDN SDG,SDG810,SDG08CBD6R0561,1.08.01.15R2,08-00-00-13-00'
        self.timeout = 100
        self.resource = None

    def connect(self):
        try:
            self.resource = pyvisa.ResourceManager().open_resource(self.addr, open_timeout=self.timeout)
            logging.info("{} is connecting...".format(self.name))
            return True
        except pyvisa.VisaIOError as ex:
            logging.info("{} is disconnect...".format(self.name))
            logging.error(ex)
            return False

    def disconnect(self):
        try:
            if self.resource:
                self.resource.close()
                logging.info("{} is closed...".format(self.name))
        except Exception as ex:
            logging.info("{} can't close ...".format(self.name))
            logging.error(ex)

    def isExist(self):
        try:
            self.resource = pyvisa.ResourceManager().open_resource(self.addr, open_timeout=self.timeout)
            logging.info(" {} is exists!".format(self.name))
            return True
        except pyvisa.VisaIOError as ex:
            logging.info("{} is not exists...".format(self.name))
            logging.error(ex)
            return False

    def write(self, msg):
        try:
            if not self.resource:
                self.connect()
            self.resource.write(msg)
            logging.info("{} receive : '{}'".format(self.name, msg))
            time.sleep(0.2)
        except Exception as ex:
            logging.info("{} can't write to...".format(self.name))
            logging.error(ex)

    def query(self, msg):
        try:
            if not self.resource:
                self.connect()
            response = self.resource.query(msg).strip()
            logging.info("{} receive : '{}'".format(self.name, msg))


            return response

        except Exception as ex:
            logging.info("{} can't query to...".format(self.name))
            logging.error(ex)

    def deviceInfo(self):
        return self.idn

    # def __del__(self):
    #     self.disconnect()

    def __repr__(self):
        return self.idn


if __name__ == '__main__':
    a =Multimeter()
    a.connect()
    print(a.query('*IDN?'))
