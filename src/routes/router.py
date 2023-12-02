from fastapi import APIRouter
from src.models.hotel_reservation import HotelReservationData
from src.controllers.predict_controller import get_predictions
from fastapi import HTTPException


router = APIRouter()


@router.get('/')
def get_main_route():
    return {'message': 'projeto em produção'}


@router.post('/api/v1/predict')
def get_predict_route(reservations_data: HotelReservationData):
    try:
        result_predict = get_predictions(reservations_data)
        return {
            'result': result_predict
        }

    except Exception as err:
        raise HTTPException(status_code=err.status_code, detail=err.detail)
