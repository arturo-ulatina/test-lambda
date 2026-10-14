import boto3
from utils.config import AWS_REGION, AWS_SSO_PROFILE
from utils.config import is_development


def get_boto_session():
    if is_development():
        return boto3.Session(profile_name=AWS_SSO_PROFILE, region_name=AWS_REGION)
    else:
        return boto3.Session()
