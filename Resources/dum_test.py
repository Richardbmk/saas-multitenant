import json

# import layer function
# remember to mark my_layer folder as source directory from PyCharm
from my_common_function import say_hello


def lambda_handler(event, context):
    message = "Hello Richard"
    return {
        "statusCode": 200,
        "message": message,
        # "body": {json.dumps({"message": say_hello()})},  # invoke layer function
    }
