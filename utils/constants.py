from enum import Enum

DEV_ENVIRONMENT = "dev"


class EnvLabels(Enum):
    AwsSsoProfile = "AWS_SSO_PROFILE"
    AwsRegion = "AWS_REGION"
    Environment = "ENVIRONMENT"
