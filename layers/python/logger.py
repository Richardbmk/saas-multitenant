from aws_lambda_powertools import Logger

logger = Logger()


def info(log_message):
    """Log info messages"""
    # logger.structure_logs(append=True, tenant_id=tenant_id)
    logger.info(log_message)


def error(log_message):
    """Log error message"""
    # logger.structure_logs(append=True, tenant_id=tenant_id)
    logger.error(log_message)


def log_with_tenant_context(event, log_message):
    """Log with tenant context. Extracts tenant context from the lambda events"""
    logger.structure_logs(
        append=True, tenant_id=event["requestContext"]["authorizer"]["tenantId"]
    )
