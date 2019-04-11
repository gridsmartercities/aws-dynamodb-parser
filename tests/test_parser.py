from unittest import TestCase
from aws_dynamodb_parser import parse


class ParserTests(TestCase):

    def testParseStringTypeInDictionary(self):
        given_data = {'String': {'S': 'Hello World!'}}
        expected_data = {'String': 'Hello World!'}

        self.assertEqual(expected_data, parse(given_data))
