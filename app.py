from aws.dynamo import put_item, scan_item, get_all_items, DynamoTables, Attr
from utils.utils import generate_uuid


def handler(event, context):

    print("Hello, U Latina!")

    print("Event", event)

    uuid: str = generate_uuid()

    student: dict = {
        "id": uuid,
        "name": event.get("name"),
        "lastname": event.get("lastname"),
        "games": event.get("games", []),
    }

    items = scan_item(
        DynamoTables.Students,
        Attr("name").eq(event.get("name")) & Attr("lastname").eq(event.get("lastname")),
    )
    if len(items) == 0:
        print("Saving new student...")
        put_item(DynamoTables.Students, student)
    else:
        print("Student already exists!")
        print(items)

    print("Getting all items...")
    items = get_all_items(DynamoTables.Students)

    print(items)

    return {"statusCode": 200, "body": "All operations finished successfully"}
