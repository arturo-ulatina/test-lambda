import json
from botocore.exceptions import ClientError
from .session import get_boto_session


def get_secrets(secret_id: str):

    session = get_boto_session()
    client = session.client(service_name="secretsmanager", region_name="us-east-1")

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_id)

        secret = get_secret_value_response["SecretString"]

        secret_dict = json.loads(secret)

        return secret_dict
    except ClientError as e:
        print(f"Error retrieving secret", str(e))
        raise e
