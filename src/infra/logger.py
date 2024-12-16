import logging


class LoggerConfig:

    @staticmethod
    def setup_logger(name: str,
                     log_file: str | None = None,
                     level: int = logging.DEBUG) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.handlers.clear()

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        if log_file:
            # here i would configure the file handler if log_file is provided.
            # leaving it empty for now
            print("Setting up file handler for logger.")
        else:
            print("Skipping file handler setup.")

        return logger

