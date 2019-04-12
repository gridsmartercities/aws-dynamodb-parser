

def parse(dynamodb_object):
    for key in dynamodb_object.keys():
        data_type = list(dynamodb_object[key].keys())[0]
        if data_type == 'S':
            dynamodb_object[key] = dynamodb_object[key][data_type]

        elif data_type == 'N':
            dynamodb_object[key] = to_num(dynamodb_object[key][data_type])

        elif data_type == 'B':
            dynamodb_object[key] = bytes(dynamodb_object[key][data_type], 'utf-8')

        elif data_type == 'SS':
            dynamodb_object[key] = dynamodb_object[key][data_type]

        elif data_type == 'NS':
            dynamodb_object[key] = [to_num(data) for data in dynamodb_object[key][data_type]]

        elif data_type == 'BS':
            dynamodb_object[key] = [bytes(data, 'utf-8') for data in dynamodb_object[key][data_type]]
    return dynamodb_object


def to_num(number):
    try:
        return int(number)
    except ValueError:
        return float(number)
