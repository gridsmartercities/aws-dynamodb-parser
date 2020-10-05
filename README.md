[<img align="right" alt="Grid Smarter Cities" src="https://s3.eu-west-2.amazonaws.com/open-source-resources/grid_smarter_cities_small.png">](https://www.gridsmartercities.com/)

![Build Status](https://codebuild.eu-west-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZGdTRFhHdng1Mks0THRaT2VkR3JYaWpOWGlwNjYvVGVYWUNoZGp6VW9MZDRMZ1I0WDFVNFJ0cHBORkJJVSswMWQ1VkxISGNFR1dWTElrWThDTVBldjUwPSIsIml2UGFyYW1ldGVyU3BlYyI6IlFMS1V1K0F5a1BHRTZlN0IiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/aws-dynamodb-parser.svg?color=brightgreen)](https://pypi.org/project/aws-dynamodb-parser/)

# AWS DynamoDB Parser

AWS DynamoDB utility for parsing DynamoDB responses

## Installation
```
pip install aws-dynamodb-parser
```

## Package Contents
### [parse](https://github.com/gridsmartercities/aws-dynamodb-parser/blob/master/aws_dynamodb_parser/utils.py#L4)
`parse` is the main method exposed for parsing DynamoDB responses when using `boto3`.

The `parse` function can handle [all of the data types AWS DynamoDB supports](https://boto3.amazonaws.com/v1/documentation/api/latest/_modules/boto3/dynamodb/types.html) as of October 2020.

## Examples
Assuming we have a table `TABLE_NAME` containing the following entries, with `id` set as the partition key and `timestamp` as the sort key.

All three fields included are strings.

|id                                  |timestamp                 |name             |
|------------------------------------|--------------------------|-----------------|
|a77b5fc0-75cb-408c-bebf-863873506cce|2020-10-01 13:13:47.388492|First test entry |
|a77b5fc0-75cb-408c-bebf-863873506cce|2020-10-01 13:15:25.376589|Second test entry|
|fa853ff0-706e-45db-b6ae-aa6a8a1f7856|2020-10-01 13:16:47.720778|Third test entry |


Parsing the result from a `get_item` request:

```py
import boto3
from aws_dynamodb_parser import parse

dynamodb_client = boto3.client("dynamodb")
response = dynamodb_client.get_item(
    TableName="TABLE_NAME",
    Key={
        "id": {"S": "a77b5fc0-75cb-408c-bebf-863873506cce"},
        "timestamp": {"S": "2020-10-01 13:13:47.388492"}
    }
)

item = response.get("Item", {})
print(item)
# {'id': {'S': 'a77b5fc0-75cb-408c-bebf-863873506cce'}, 'timestamp': {'S': '2020-10-01 13:13:47.388492'}, 'name': {'S': 'First test entry'}}

entry = parse(item)
print(entry)
# {'id': 'a77b5fc0-75cb-408c-bebf-863873506cce', 'timestamp': '2020-10-01 13:13:47.388492', 'name': 'First test entry'}
```

Parsing the result from a `query` request:

```py
import boto3
from aws_dynamodb_parser import parse

dynamodb_client = boto3.client("dynamodb")
response = dynamodb_client.query(
    TableName="TABLE_NAME",
    KeyConditionExpression="#id = :id",
    ExpressionAttributeNames={
        "#id": "id"
    },
    ExpressionAttributeValues={
        ":id": {"S": "a77b5fc0-75cb-408c-bebf-863873506cce"}
    }
)

items = response.get("Items", [])
print(items)
# [{'id': {'S': 'a77b5fc0-75cb-408c-bebf-863873506cce'}, 'timestamp': {'S': '2020-10-01 13:13:47.388492'}, 'name': {'S': 'First test entry'}}, {'id': {'S': 'a77b5fc0-75cb-408c-bebf-863873506cce'}, 'timestamp': {'S': '2020-10-01 13:15:25.376589'}, 'name': {'S': 'Second test entry'}}]

entries = parse(items)
print(entries)
# [{'id': 'a77b5fc0-75cb-408c-bebf-863873506cce', 'timestamp': '2020-10-01 13:13:47.388492, 'name': 'First test entry'}, {'id': 'a77b5fc0-75cb-408c-bebf-863873506cce', 'timestamp': '2020-10-01 13:15:25.376589', 'name': 'Second test entry'}]
```

## Documentation
Users can get the docstring help by running:
```py
from aws_dynamodb_parser import parse
help(parse)
```

## Links
- [Github](https://github.com/gridsmartercities/aws-dynamodb-parser)
- [PyPI](https://pypi.org/project/aws-dynamodb-parser/)
- [Test PyPI](https://test.pypi.org/project/aws-dynamodb-parser/)