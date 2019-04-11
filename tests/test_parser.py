from unittest import TestCase
from aws_dynamodb_parser import parse


class ParserTests(TestCase):

    def testParseStringTypeInDictionary(self):
        given_data = {'String': {'S': 'Hello World!'}}
        expected_data = {'String': 'Hello World!'}

        self.assertEqual(expected_data, parse(given_data))

    def testParseIntegerTypeInDictionary(self):
        given_data = {'Number': {'N': '1337'}}
        expected_data = {'Number': 1337}

        self.assertEqual(expected_data, parse(given_data))

    def testParseFloatTypeInDictionary(self):
        given_data = {'Number': {'N': '13.37'}}
        expected_data = {'Number': 13.37}

        self.assertEqual(expected_data, parse(given_data))
