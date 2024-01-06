import logging

from pythonapp.util.date import get_current_date
from pythonapp.util.logs import init_logger


def main():
    """Application entry point."""

    init_logger()
    logger = logging.getLogger(__name__)

    logger.info('formatting the date')
    today = get_current_date()
    logger.info('retrieved the date: %s', today)

    print(f'Today is {today}.')


if __name__ == '__main__':
    main()
