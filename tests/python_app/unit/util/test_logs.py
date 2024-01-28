import json
import logging

import pytest
import toml
from python_app.util.logs import LoggerSetup


@pytest.fixture()
def app_config(tmp_path):
    config_path = tmp_path / 'config'
    config_path.mkdir()
    app_config_file = config_path / 'test_config.toml'

    # create an empty app config
    with open(str(app_config_file), 'w') as f:
        toml.dump({}, f)

    return app_config_file


@pytest.fixture
def app_config_with_logfile(tmp_path):
    config_path = tmp_path / 'config'
    config_path.mkdir()
    app_config_file = config_path / 'test_config.toml'
    app_log_file = config_path / 'test.log'

    # create an app config that specifies a log file
    with open(str(app_config_file), 'w') as f:
        toml.dump({'tool': {'python_app': {'log_file': str(app_log_file)}}}, f)

    return app_config_file, app_log_file


def test_no_logfile(app_config, caplog):
    config_file = app_config
    logger_setup = LoggerSetup('pythonapptest', str(config_file))
    logger_setup.init_logger()

    # ensure that the logger's streamhandler is intact, even if there's
    # no log file specified in the config (a bit of overkill, but leaving as
    # an example of pytest's caplog fixture))
    logger = logging.getLogger('pythonapptest')
    logger.info('howdy')
    assert len(caplog.records) == 1


def test_logfile(app_config_with_logfile):
    config_file, log_file = app_config_with_logfile
    logger_setup = LoggerSetup('pythonapptest', str(config_file))
    logger_setup.init_logger()

    # verify that log init created the log file
    assert log_file.exists()

    # create a log entry to test
    logger = logging.getLogger('pythonapptest')
    logger.info('howdy')
    log_contents = log_file.read_text()

    # there should be one line in the log file
    assert log_contents.count('\n') == 1

    # verify that the log file contents are in JSON format
    try:
        json.loads(log_contents)
    except json.JSONDecodeError:
        pytest.fail('Log file contents are not in JSON format')
