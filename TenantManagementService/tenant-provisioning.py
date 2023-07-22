import json

# import layer function
# remember to mark my_layer folder as source directory from PyCharm
from my_common_function import say_hello


def provision_tenant(event, context):
    message = "Hello Richard"
    return {
        "statusCode": 200,
        "message": message,
    }


def deprovision_tenant(event, context):
    message = "Hello Richard"
    return {
        "statusCode": 200,
        "message": message,
    }
