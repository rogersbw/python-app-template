import logging

from python_app.util.date import get_current_date
from python_app.util.logs import LoggerSetup


def main():
    """Application entry point."""

    LoggerSetup('python_app').init_logger()
    logger = logging.getLogger(__name__)

    logger.info('formatting the date')
    today = get_current_date()
    logger.info('retrieved the date: %s', today)

    return today


def say_hello():
    return 'howdy'


if __name__ == '__main__':
    today = main()
    print(f'Today is {today}.')
