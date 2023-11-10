import datetime

from Tools.Interfaces import BASE_DIR
import logging

from logging.handlers import RotatingFileHandler

LOG_FORMAT = "%(asctime)s - %(filename)s %(funcName)s() [line:%(lineno)d] %(levelname)s - %(message)s"

sh = logging.StreamHandler()
tfh = logging.handlers.TimedRotatingFileHandler(
    BASE_DIR + rf"\_Logs\{datetime.datetime.now().strftime('%Y-%m-%d')}.log",
    when='D', interval=1, backupCount=0, encoding='UTF-8')
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO, handlers=[tfh, sh])
# logging.DEBUG,logging.INFO,logging.CRITICAL
logging.getLogger('__name__')
# logging.debug(xxx)中的内容为message，而我们设置的format就是message如何和其他的信息结合，比如我们想有记录日志的时间戳等
if __name__ == '__main__':
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')
    #
# # 这样会记录得到
# 23-04-09 12:10:32 root:DEBUG:This is a debug message
# 23-04-09 12:10:32 root:INFO:This is an info message
# 23-04-09 12:10:32 root:WARNING:This is a warning message
# 23-04-09 12:10:32 root:ERROR:This is an error message
# 23-04-09 12:10:32 root:CRITICAL:This is a critical message
