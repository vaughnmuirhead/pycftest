import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GetRequest():

    def __init__(self, payload_dict, header_dict=None, *args, **kwargs):
        logger.info('Init {0}...'.format(__name__))
        self.payload_dict = payload_dict
        self.args = payload_dict
        self.headers = header_dict

    def get_json(self):
        message = 'Getting json...'
        logger.info(message)
        js = self.payload_dict
        message = 'Returning json.'
        logger.info(message)
        return(js)
