from .session import get_boto_session
from boto3.dynamodb.conditions import Key, Attr
from enum import Enum


class DynamoTables(Enum):
    Students = "Students"


def get_table(table: DynamoTables):
    session = get_boto_session()
    dynamodb = session.resource("dynamodb")

    return dynamodb.Table(table.value)


def put_item(table: DynamoTables, item: dict):
    tbl = get_table(table)

    tbl.put_item(Item=item)


def scan_item(table: DynamoTables, filters):
    tbl = get_table(table)

    response = tbl.scan(FilterExpression=filters)

    return response["Items"]


def get_all_items(table: DynamoTables):
    tbl = get_table(table)

    response = tbl.scan()

    return response["Items"]
