from freezegun import freeze_time
from python_app.app import main


@freeze_time('2019-07-13')
def test_main_date():
    output = main()
    assert output == 'July 13, 2019'
