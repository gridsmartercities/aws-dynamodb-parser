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
        expected_data = {'Bytes': b'this text is base64-encoded'}

        self.assertEqual(expected_data, parse(given_data))

    def test_parse_string_set_in_dictionary(self):
        given_data = {'StringSet': {'SS': ['Hello', 'World', '!']}}
        expected_data = {'StringSet': ['Hello', 'World', '!']}

        self.assertEqual(expected_data, parse(given_data))

    def test_parse_number_set_in_dictionary(self):
        given_data = {'NumberSet': {'NS': ['1337', '13.37']}}
        expected_data = {'NumberSet': [1337, 13.37]}

        self.assertEqual(expected_data, parse(given_data))

    def test_parse_byte_set_in_dictionary(self):
        given_data = {'ByteSet': {'BS': ['U3Vubnk=', 'UmFpbnk=']}}
        expected_data = {'ByteSet': [b'Sunny', b'Rainy']}

        self.assertEqual(expected_data, parse(given_data))

    def test_parse_map_in_dictionary(self):
        given_data = {
            'Map': {
                'M': {
                    'String': {'S': 'Hello World!'},
                    'Integer': {'N': '1337'},
                    'Float': {'N': '13.37'},
                    'Bytes': {'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'},
                    'StringSet': {'SS': ['Hello', 'World', '!']},
                    'NumberSet': {'NS': ['1337', '13.37']},
                    'ByteSet': {'BS': ['U3Vubnk=', 'UmFpbnk=']}
                }
            }
        }
        expected_data = {
            'Map': {
                'String': 'Hello World!',
                'Integer': 1337,
                'Float': 13.37,
                'Bytes': b'this text is base64-encoded',
                'StringSet': ['Hello', 'World', '!'],
                'NumberSet': [1337, 13.37],
                'ByteSet': [b'Sunny', b'Rainy']
            }
        }

        self.assertEqual(expected_data, parse(given_data))

    def test_parse_list_in_dictionary(self):
        given_data = {
            'List': {
                'L': [
                    {'S': 'Hello World!'},
                    {'N': '1337'},
                    {'N': '13.37'},
                    {'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'},
                    {'SS': ['Hello', 'World', '!']},
                    {'NS': ['1337', '13.37']},
                    {'BS': ['U3Vubnk=', 'UmFpbnk=']}
                ]
            }
        }
        expected_data = {
            'List': ['Hello World!', 1337, 13.37, b'this text is base64-encoded', ['Hello', 'World', '!'],
                     [1337, 13.37], [b'Sunny', b'Rainy']]
        }

        self.assertEqual(expected_data, parse(given_data))

    def test_parse_null_type_in_dictionary(self):
        given_data = {'DoesntExist': {'NULL': True}}
        expected_data = {'DoesntExist': None}

        self.assertEqual(expected_data, parse(given_data))

    def test_parse_bool_type_in_dictionary(self):
        given_data = {
            'BoolTrue': {'BOOL': True},
            'BoolFalse': {'BOOL': False}
        }
        expected_data = {'BoolTrue': True, 'BoolFalse': False}

        self.assertEqual(expected_data, parse(given_data))

    def test_parse_multiple_types_in_dictionary(self):
        given_data = {
            'String': {'S': 'Hello World!'},
            'Integer': {'N': '1337'},
            'Float': {'N': '13.37'},
            'Bytes': {'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'},
            'StringSet': {'SS': ['Hello', 'World', '!']},
            'NumberSet': {'NS': ['1337', '13.37']},
            'ByteSet': {'BS': ['U3Vubnk=', 'UmFpbnk=']},
            'Map': {
                'M': {
                    'String': {'S': 'Hello World!'},
                    'Integer': {'N': '1337'},
                    'Float': {'N': '13.37'},
                    'Bytes': {'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'},
                    'StringSet': {'SS': ['Hello', 'World', '!']},
                    'NumberSet': {'NS': ['1337', '13.37']},
                    'ByteSet': {'BS': ['U3Vubnk=', 'UmFpbnk=']}
                }
            },
            'List': {
                'L': [
                    {'S': 'Hello World!'},
                    {'N': '1337'},
                    {'N': '13.37'},
                    {'B': 'dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk'},
                    {'SS': ['Hello', 'World', '!']},
                    {'NS': ['1337', '13.37']},
                    {'BS': ['U3Vubnk=', 'UmFpbnk=']}
                ]
            },
            'DoesntExist': {'NULL': True},
            'BoolTrue': {'BOOL': True},
            'BoolFalse': {'BOOL': False}
        }
        expected_data = {
            'String': 'Hello World!',
            'Integer': 1337,
            'Float': 13.37,
            'Bytes': b'this text is base64-encoded',
            'StringSet': ['Hello', 'World', '!'],
            'NumberSet': [1337, 13.37],
            'ByteSet': [b'Sunny', b'Rainy'],
            'Map': {
                'String': 'Hello World!',
                'Integer': 1337,
                'Float': 13.37,
                'Bytes': b'this text is base64-encoded',
                'StringSet': ['Hello', 'World', '!'],
                'NumberSet': [1337, 13.37],
                'ByteSet': [b'Sunny', b'Rainy']
            },
            'List': ['Hello World!', 1337, 13.37, b'this text is base64-encoded', ['Hello', 'World', '!'],
                     [1337, 13.37], [b'Sunny', b'Rainy']],
            'DoesntExist': None,
            'BoolTrue': True,
            'BoolFalse': False
        }

        self.assertEqual(expected_data, parse(given_data))

    def test_parse_unknown_type_in_dictionary(self):
        given_data = {
            'Unknown': {'Q': 'Quanta'}
        }

        self.assertRaises(TypeError, parse, given_data)
