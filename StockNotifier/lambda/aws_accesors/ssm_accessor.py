import boto3
from botocore.exceptions import ClientError

ssm = boto3.client('ssm')

def retrieve_parameter(parameter: str) -> str:
    try:
        response = ssm.get_parameter(
            Name=parameter,
            WithDecryption=True
        )
        value = response['Parameter']['Value']
        print(f"Retrieved {parameter} from parameter store: {value}")
        return value
    except ClientError as e:
        if e.response['Error']['Code'] == 'ParameterNotFound':
            print("Parameter does not exist")
        else:
            print(f"Error retrieving parameter {e}")
        raise e