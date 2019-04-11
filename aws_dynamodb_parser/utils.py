

def parse(dynamodb_object):
    for key in dynamodb_object.keys():
        dynamodb_object[key] = dynamodb_object[key]['S']

    return dynamodb_object
