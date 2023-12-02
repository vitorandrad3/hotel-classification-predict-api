from src.utils.functions.process_prediction_data import process_data
from src.sagemaker_configuration.predict_model_configuration import client
from botocore.exceptions import (
    ValidationError,
    DataNotFoundError,
    DataNotFoundError,
    UnknownRegionError,
    ConnectionError,
    NoCredentialsError,
    ClientError,
)
from fastapi import HTTPException
from os import getenv as env


def get_predictions(reservations_data):
    try:
        formated_data = process_data(reservations_data)
        predict = client.invoke_endpoint(
            EndpointName=env("ENDPOINT"), Body=formated_data, ContentType="text/csv"
        )

        predict_value = int(float(predict["Body"].read().decode("utf-8")) + 1)

        return predict_value

    except ValidationError as err:
        raise HTTPException(status_code=401, detail=str(err))
    except DataNotFoundError as err:
        raise HTTPException(status_code=404, detail=str(err))
    except NoCredentialsError as err:
        raise HTTPException(status_code=401, detail=str(err))
    except ClientError as err:
        raise HTTPException(status_code=400, detail=str(err))
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))
