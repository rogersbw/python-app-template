import json
import logging
import traceback


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_dict = record.__dict__.copy()

        log_dict['args'] = [str(arg) for arg in record.args]
        log_dict['msg'] = record.getMessage()

        # if there's exception info, include it
        if record.exc_info:
            exception = traceback.format_exception(*record.exc_info)
            log_dict['exc_info'] = exception

        return json.dumps(log_dict)


def init_logger():
    logger = logging.getLogger('pythonapp')
    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter())
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
