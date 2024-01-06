from pythonapp.util.date import get_current_date


def main():
    """Application entry point."""

    today = get_current_date()
    print(f'Today is {today}.')


if __name__ == '__main__':
    main()
