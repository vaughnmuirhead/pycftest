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

    def test_get_headers(self):
        payload_dict = {"key": "value"}
        header_dict = {"headerKey": "headerValue"}
        req = cft.GetRequest(payload_dict=payload_dict, header_dict=header_dict)
        headers = req.headers
        self.assertIn('headerKey', headers)

if __name__ == '__main__':
    unittest.main()
