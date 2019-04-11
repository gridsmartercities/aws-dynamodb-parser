from unittest import TestCase
from aws_dynamodb_parser import parse


class ParserTests(TestCase):

    def test_parse_string_type_in_dictionary(self):
        given_data = {'String': {'S': 'Hello World!'}}
        expected_data = {'String': 'Hello World!'}

        self.assertEqual(expected_data, parse(given_data))

    def test_parse_integer_type_in_dictionary(self):
        given_data = {'Number': {'N': '1337'}}
        expected_data = {'Number': 1337}

        self.assertEqual(expected_data, parse(given_data))

    def test_parse_float_type_in_dictionary(self):
        given_data = {'Number': {'N': '13.37'}}
        expected_data = {'Number': 13.37}

        self.assertEqual(expected_data, parse(given_data))

    def test_parse_bytes_type_in_dictionary(self):
        given_data = {'Bytes': {'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'}}
        expected_data = {'Bytes': b'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'}

        self.assertEqual(expected_data, parse(given_data))

    def test_parse_multiple_types_in_dictionary(self):
        given_data = {
            'String': {'S': 'Hello World!'},
            'Integer': {'N': '1337'},
            'Float': {'N': '13.37'},
            'Bytes': {'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'}
        }
        expected_data = {
            'String': 'Hello World!',
            'Integer': 1337,
            'Float': 13.37,
            'Bytes': b'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'
        }

        self.assertEqual(expected_data, parse(given_data))
