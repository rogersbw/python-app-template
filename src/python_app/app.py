import structlog

from python_app.util.date import get_current_date
from python_app.util.logs import setup_logging

setup_logging()
logger = structlog.get_logger()


def main():
    """Application entry point."""

    today = get_current_date()
    logger.info('retrieved the date: %s', today)

    return today


def say_hello():
    return 'howdy'


if __name__ == '__main__':
    today = main()
    print(f'Today is {today}.')
