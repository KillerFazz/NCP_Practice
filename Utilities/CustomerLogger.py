import logging

class LogGen:
    @staticmethod
    def Loggen():
        logging.basicConfig(filename=".\\LogFiles\\Automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d%y %I:%M:%S %P')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

