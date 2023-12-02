from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_read_main_route():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'esse é o projeto da equipe 1'}


def test_read_predict_route_succes():
    response = client.post('/api/v1/predict',
                           json={
                               "no_of_adults": 2,
                               "no_of_children": 0,
                               "no_of_weekend_nights": 1,
                               "no_of_week_nights": 2,
                               "type_of_meal_plan": "Meal Plan 1",
                               "required_car_parking_space": 0,
                               "room_type_reserved": "Room_Type 1",
                               "lead_time": 224,
                               "arrival_year": 2017,
                               "arrival_month": 10,
                               "arrival_date": 2,
                               "market_segment_type": "Offline",
                               "repeated_guest": 0,
                               "no_of_previous_cancellations": 0,
                               "no_of_previous_bookings_not_canceled": 0,
                               "no_of_special_requests": 0,
                               "booking_status": "Not_Canceled"
                           }
                           )

    assert response.status_code == 200
    assert response.json() == {
        "result": 1
    }


def test_read_predict_route_with_error():
    response = client.post('/api/v1/predict',
                           json={
                               "no_of_adults": 2,
                               "no_of_children": 0,
                               "no_of_weekend_nights": 1,
                               "no_of_week_nights": 2,
                               # teste com um plano de refeição fora do escopo (permitido apenas do 1-7, por exemplo) - gera uma coluna a mais
                               "type_of_meal_plan": "Meal Plan 8",
                               "required_car_parking_space": 0,
                               "room_type_reserved": "Room_Type 1",
                               "lead_time": 224,
                               "arrival_year": 2017,
                               "arrival_month": 10,
                               "arrival_date": 2,
                               "market_segment_type": "Offline",
                               "repeated_guest": 0,
                               "no_of_previous_cancellations": 0,
                               "no_of_previous_bookings_not_canceled": 0,
                               "no_of_special_requests": 0,
                               "booking_status": "Not_Canceled"
                           }
                           )

    assert response.status_code == 400
    assert response.json() == {'detail': 'An error occurred (ModelError) when calling the InvokeEndpoint operation: Received client error (400) from primary with message \"Unable to evaluate payload provided: Feature size of csv inference data 32 is not consistent with feature size of trained model 31\". See https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#logEventViewer:group=/aws/sagemaker/Endpoints/xgboost-2023-09-15-16-19-16-544 in account 429789586118 for more information.'}
