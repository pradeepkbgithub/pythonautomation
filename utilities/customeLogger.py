import logging


class LogGen:

    @staticmethod
    def loggen():
        print('+++++++++++++++++++++++++++++pkb+++++++++++++++++++++++++++++++++')
        #logging.basicConfig(filename=".\\Logs\\automation.log", format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        #logging.basicConfig(filename='.\\Logs\\automation.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',force=True)
        logging.basicConfig(filename='.\\Logs\\automation.log', filemode='w',
                            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger