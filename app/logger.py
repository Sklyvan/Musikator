from configuration import CONFIGURATION
import logging

def startLogger() -> logging.Logger:
    """
    Starts the logger with the configuration from the configuration file. The logger will log the messages to the file
    defined in the INI configuration file with the specified log level and format. It will also log to the console.
    """
    logLevel = CONFIGURATION.get('LOGGING', 'LEVEL', fallback='INFO').upper()
    logFormat = CONFIGURATION.get('LOGGING', 'FORMAT', fallback='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logFile = CONFIGURATION.get('LOGGING', 'FILE_NAME', fallback='app.log')

    logger = logging.getLogger(__name__)
    logger.setLevel(logLevel)

    # File handler
    file_handler = logging.FileHandler(logFile)
    file_handler.setFormatter(logging.Formatter(logFormat))
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(logFormat))
    logger.addHandler(console_handler)

    return logger

LOGGER = startLogger()
