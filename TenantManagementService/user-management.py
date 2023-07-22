import json

# import layer function
# remember to mark my_layer folder as source directory from PyCharm
from my_common_function import say_hello


def create_user(event, context):
    message = "Hello Richard"
    return {
        "statusCode": 200,
        "message": message,
    }


def get_users(event, context):
    message = "Hello Richard"
    return {
        "statusCode": 200,
        "message": message,
    }


def get_user(event, context):
    message = "Hello Richard"
    return {
        "statusCode": 200,
        "message": message,
    }


def update_user(event, context):
    message = "Hello Richard"
    return {
        "statusCode": 200,
        "message": message,
    }


def disable_user(event, context):
    message = "Hello Richard"
    return {
        "statusCode": 200,
        "message": message,
    }


def disable_user_by_tenant(event, context):
    message = "Hello Richard"
    return {
        "statusCode": 200,
        "message": message,
    }


def enable_user_by_tenant(event, context):
    message = "Hello Richard"
    return {
        "statusCode": 200,
        "message": message,
    }


def get_user_info(event, context):
    message = "Hello Richard"
    return {
        "statusCode": 200,
        "message": message,
    }


def create_tenant_admin_user(event, context):
    message = "Hello Richard"
    return {
        "statusCode": 200,
        "message": message,
    }
