import logging

from api.config import conf


def get_logger(name: str | None = None, level: int = logging.INFO):
    logger = logging.getLogger()
    logger.setLevel(level=level)

    if not name:
        logging.basicConfig(format="%(level)s %(asctime)s - %(message)s", level=level)
    else:
        logging.basicConfig(
            format=f"%(level)s %(asctime)s - {name} - %(message)s", level=level
        )

    if conf.ENV == "TEST":
        logger.setLevel(logging.WARN)

    return logger
