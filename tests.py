import unittest
from unittest.mock import patch

from sorting import parse_data


class SortingTest(unittest.TestCase):

    def setUp(self):
        self.test_data = {
            "id": 1,
            "name": "test",
            "children": [],
        }
        self.output = []

    @patch('sorting.read_json')
    def test_read_json(self, mock_read_json):
        mock_read_json.return_value = self.test_data
        self.assertEqual( mock_read_json(), self.test_data)
        mock_read_json.assert_called_once()

    def test_parse_data(self):
        parse_data(element=self.test_data,
                   output=self.output)
        self.assertEqual(self.output[0].get('id'), self.test_data.get('id'))
        self.assertEqual(self.output[0].get('ids'), [self.test_data.get('id')])
        self.assertEqual(self.output[0].get('name'), self.test_data.get('name'))
        self.assertEqual(self.output[0].get('tree'), self.test_data.get('name'))
        self.assertEqual(self.output[0].get('level'), 1)
        self.assertIsNone(self.output[0].get('parrent_id'))


if __name__ == "__main__":
    unittest.main()
