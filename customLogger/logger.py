import logging
from logging.handlers import RotatingFileHandler

class CustomLogger:
    _shared_logger = None  # Singleton for the logger instance

    @staticmethod
    def get_logger(log_file: str = "app.log", level: int = logging.DEBUG):
        """
        Returns a shared logger instance that writes to a single log file.
        :param log_file: Path to the log file (default: 'app.log').
        :param level: Logging level (default: DEBUG).
        :return: Logger instance.
        """
        if CustomLogger._shared_logger is None:
            # Initialize the shared logger
            logger = logging.getLogger("shared_logger")
            logger.setLevel(level)

            # Prevent duplicate handlers
            if not logger.hasHandlers():
                # File handler with log rotation
                file_handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=2)
                file_handler.setLevel(level)

                # Console handler for debugging
                console_handler = logging.StreamHandler()
                console_handler.setLevel(level)

                # Define log format
                formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                file_handler.setFormatter(formatter)
                console_handler.setFormatter(formatter)

                # Add handlers to the logger
                logger.addHandler(file_handler)
                logger.addHandler(console_handler)

            CustomLogger._shared_logger = logger

        return CustomLogger._shared_logger
