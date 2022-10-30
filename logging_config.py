#logging 설정
import logging

Log_Format = "%(levelname)s %(asctime)s     %(message)s"

logging.basicConfig(filename = "logfile.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.INFO)

logger = logging.getLogger()