import unittest
from . import CFtest as cft
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestMain(unittest.TestCase):

    def test_get_json(self):
        payload_dict = {"key": "value"}
        req = cft.GetRequest(payload_dict)
        args = req.get_json()
        self.assertIn('key', args)
        self.assertEqual('value', args.get('key'))

    def test_get_headers(self):
        payload_dict = {"key": "value"}
        header_dict = {"headerKey": "headerValue"}
        method = 'POST'
        req = cft.GetRequest(payload_dict=payload_dict, method=method, header_dict=header_dict)
        headers = req.headers
        self.assertIn('headerKey', headers)
        self.assertEqual(header_dict['headerKey'], headers.get('headerKey'))

    def test_get_method(self):
        logger.info('Testing get_method...')
        payload_dict = {"key": "value"}
        header_dict = {"headerKey": "headerValue"}
        method = 'POST'
        req = cft.GetRequest(payload_dict=payload_dict, method=method, header_dict=header_dict)
        method = req.method
        self.assertEqual('POST', req.method)  

if __name__ == '__main__':
    unittest.main()
