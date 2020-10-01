import base64
from typing import Any, Union


def parse(dynamodb_object: Union[dict, list]) -> dict:
    if isinstance(dynamodb_object, list):
        return [parse(obj) for obj in dynamodb_object]

    parsed = {}
    for key in dynamodb_object.keys():
        parsed[key] = _parse_pair(dynamodb_object[key])
    return parsed


# pylint:disable=too-many-return-statements
def _parse_pair(type_value_pair: dict) -> Any:
    data_type = list(type_value_pair.keys())[0]

    if data_type in {"S", "SS", "BOOL"}:
        return type_value_pair[data_type]

    if data_type == "N":
        return _to_num(type_value_pair[data_type])

    if data_type == "NS":
        return [_to_num(data) for data in type_value_pair[data_type]]

    if data_type == "B":
        return base64.decodebytes(bytes(type_value_pair[data_type], "utf-8"))

    if data_type == "BS":
        return [base64.decodebytes(bytes(data, "utf-8")) for data in type_value_pair[data_type]]

    if data_type == "M":
        return parse(type_value_pair[data_type])

    if data_type == "L":
        return [_parse_pair(item) for item in type_value_pair[data_type]]

    if data_type == "NULL" and type_value_pair[data_type]:
        return None

    raise TypeError("Unknown DynamoDB data type '%s' with value '%s'" % (data_type, type_value_pair[data_type]))


def _to_num(number: Any) -> Union[float, int]:
    try:
        return int(number)
    except ValueError:
        return float(number)
