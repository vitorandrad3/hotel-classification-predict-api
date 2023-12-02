from src.controllers.predict_controller import get_predictions
from src.tests.mocked_data.hotel_reservations_objects import reservation_data_test1,reservation_data_test2,reservation_data_test3

def test_get_predictions():

    assert get_predictions(reservation_data_test1) == 1
    assert get_predictions(reservation_data_test2) == 2
    assert get_predictions(reservation_data_test3) == 3
