import json
import boto3
import logger

from crhelper import CfnResoruce

helper = CfnResoruce()

try:
    dynamodb = boto3.resource("dynamodb")
except Exception as e:
    helper.init_failure(e)


@helper.create
@helper.update
def do_action(event, _):
    """Called as part of bootstrap template.
    Inserts/Updates Settings table based upon the resources deployed inside
    bootstrap template
    We use these settings inside tenant template

    Args:
            event ([type]): [description]
            _ ([type]): [description]
    """
    logger.info("Updating settings")

    settings_table_name = event["ResourceProperties"]["SettingsTableName"]
    cognitoUserPoolId = event["ResourceProperties"]["cognitoUserPoolId"]
    cognitoUserPoolClientId = event["ResourceProperties"]["cognitoUserPoolClientId"]

    table_system_setting = dynamodb.Table(settings_table_name)

    response = table_system_setting.put_item(
        Item={"settingName": "userPoolId-pooled", "settingValue": cognitoUserPoolId}
    )

    response = table_system_setting.put_item(
        Item={
            "settingName": "appClientId-pooled",
            "settingValue": cognitoUserPoolClientId,
        }
    )


@helper.delete
def do_nothing(_, __):
    pass


def handler(event, context):
    helper(event, context)
