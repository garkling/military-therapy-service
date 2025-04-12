import logging


def get_logger(name: str, level: int = logging.INFO):
    logger = logging.getLogger()
    logger.setLevel(level=level)

    logging.basicConfig(format=f"%(level)s %(asctime)s - {name} - %(message)s", level=level)

    return logger
