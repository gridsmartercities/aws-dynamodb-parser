import base64
from typing import Any, Union


def parse(dynamodb_object: Union[dict, list]) -> Union[dict, list]:
    if isinstance(dynamodb_object, list):
        return [parse(obj) for obj in dynamodb_object]

    return {key: _parse_property(value) for key, value in dynamodb_object.items()}


# pylint:disable=too-many-return-statements
def _parse_property(prop: dict) -> Any:
    data_type = next(iter(prop))
    value = prop.get(data_type, [])

    if data_type in {"S", "SS", "BOOL"}:
        return value

    if data_type == "N":
        return _to_num(value)

    if data_type == "NS":
        return [_to_num(item) for item in value]

    if data_type == "B":
        return _to_bytes(value)

    if data_type == "BS":
        return [_to_bytes(item) for item in value]

    if data_type == "M":
        return parse(value)

    if data_type == "L":
        return [_parse_property(item) for item in value]

    if data_type == "NULL" and value:
        return None

    raise TypeError("Unknown DynamoDB data type '%s' with value '%s'" % (data_type, value))


def _to_num(value: Any) -> Union[float, int]:
    try:
        return int(value)
    except ValueError:
        return float(value)


def _to_bytes(value: Any) -> bytes:
    return base64.decodebytes(bytes(value, "utf-8"))
