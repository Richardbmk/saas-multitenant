import json

# import layer function
# remember to mark my_layer folder as source directory from PyCharm
from my_common_function import say_hello


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({"message": say_hello()}),  # invoke layer function
    }
