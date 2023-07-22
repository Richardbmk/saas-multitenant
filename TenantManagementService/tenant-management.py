import json

# import layer function
# remember to mark my_layer folder as source directory from PyCharm
from my_common_function import say_hello


def activate_tenant(event, context):
    message = "Hello Richard"
    return {
        "statusCode": 200,
        "message": message,
    }


def create_tenant(event, context):
    message = "Hello Richard"
    return {
        "statusCode": 200,
        "message": message,
    }


def get_tenant(event, context):
    message = "Hello Richard"
    return {
        "statusCode": 200,
        "message": message,
    }


def get_tenants(event, context):
    message = "Hello Richard"
    return {
        "statusCode": 200,
        "message": message,
    }


def update_tenant(event, context):
    message = "Hello Richard"
    return {
        "statusCode": 200,
        "message": message,
    }


def deactivate_tenant(event, context):
    message = "Hello Richard"
    return {
        "statusCode": 200,
        "message": message,
    }
