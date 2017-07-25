
import unittest
import unittest.mock as mock

from pinnacle.utils import check_status_code, clean_locals, to_camel_case
from pinnacle.exceptions import StatusCodeError


class UtilsTest(unittest.TestCase):

    def test_check_status_code_ok(self):
        resp = mock.Mock()
        resp.status_code = 200

        assert check_status_code(resp) is None

    def test_check_status_code_fail(self):
        resp = mock.Mock()
        resp.status_code = 400

        with self.assertRaises(StatusCodeError):
            check_status_code(resp)

    def test_convert_to_camel_case(self):
        assert to_camel_case('hello_world') == 'helloWorld'

    def test_clean_locals(self, test_val=None, filter=123):
        params = clean_locals(locals())
        assert params == {'filter': 123}
