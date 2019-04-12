import base64


def parse(dynamodb_object):
    for key in dynamodb_object.keys():
        dynamodb_object[key] = parse_pair(dynamodb_object[key])
    return dynamodb_object


def parse_pair(type_value_pair):  # noqa: pylint - too-many-return-statements
    data_type = list(type_value_pair.keys())[0]

    if data_type in ('S', 'SS', 'BOOL'):
        return type_value_pair[data_type]

    if data_type == 'N':
        return to_num(type_value_pair[data_type])

    if data_type == 'NS':
        return [to_num(data) for data in type_value_pair[data_type]]

    if data_type == 'B':
        return base64.decodebytes(bytes(type_value_pair[data_type], 'utf-8'))

    if data_type == 'BS':
        return [base64.decodebytes(bytes(data, 'utf-8')) for data in type_value_pair[data_type]]

    if data_type == 'M':
        return parse(type_value_pair[data_type])

    if data_type == 'L':
        return [parse_pair(item) for item in type_value_pair[data_type]]

    if data_type == 'NULL' and type_value_pair[data_type]:
        return None

    raise TypeError('Unknown DynamoDB data type \'%s\' with value \'%s\'' % (data_type, type_value_pair[data_type]))


def to_num(number):
    try:
        return int(number)
    except ValueError:
        return float(number)
