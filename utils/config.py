import os
from dotenv import load_dotenv
from .constants import EnvLabels, DEV_ENVIRONMENT

load_dotenv()

AWS_SSO_PROFILE = os.getenv(EnvLabels.AwsSsoProfile.value)
AWS_REGION = os.getenv(EnvLabels.AwsRegion.value)
ENVIRONMENT = os.getenv(EnvLabels.Environment.value)


def is_development():
    return ENVIRONMENT == DEV_ENVIRONMENT
