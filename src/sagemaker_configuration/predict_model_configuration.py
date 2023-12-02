import boto3
from os import getenv as env
from dotenv import load_dotenv

load_dotenv()

boto_session = boto3.Session(aws_access_key_id=env('AWS_ACESS_KEY'),
aws_secret_access_key=env('AWS_SECRET_ACCES_KEY'),
region_name = env('AWS_REGION'))

client = boto_session.client(service_name = 'sagemaker-runtime', region_name = env('AWS_REGION'))