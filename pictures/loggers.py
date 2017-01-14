import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s')


def logger_from(name):
    return logging.getLogger(name)
