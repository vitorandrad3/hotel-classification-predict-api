from src.utils.functions.process_prediction_data import process_data
from src.tests.mocked_data.hotel_reservations_objects import reservation_data_test1,reservation_data_test2,reservation_data_test3


def test_process_data():

    assert process_data(reservation_data_test1) == '2,0,1,2,0,224,2017,10,2,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1\r\n'
    assert process_data(reservation_data_test2) == '3,2,4,2,2,224,2017,10,2,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1\r\n'
    assert process_data(reservation_data_test3) == '3,0,2,6,0,85,2018,8,3,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1\r\n'
