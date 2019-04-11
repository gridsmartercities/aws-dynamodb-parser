

def parse(dynamodb_object):
    for key in dynamodb_object.keys():
        data_type = list(dynamodb_object[key].keys())[0]
        if data_type == 'S':
            dynamodb_object[key] = str(dynamodb_object[key][data_type])
        elif data_type == 'N':
            try:
                dynamodb_object[key] = int(dynamodb_object[key][data_type])
            except ValueError:
                dynamodb_object[key] = float(dynamodb_object[key][data_type])

    return dynamodb_object
