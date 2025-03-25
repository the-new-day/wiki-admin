import logging

def setup_logger(verbose=False, disable_logging=False):
    logger = logging.getLogger("WikiScript")
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)

    while logger.hasHandlers():
        logger.handlers.clear()

    if not disable_logging:
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        file_handler = logging.FileHandler("wiki-admin.log", encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        if verbose:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

    return logger
