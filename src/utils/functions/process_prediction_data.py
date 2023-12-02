import pandas as pd
import numpy as np
from src.utils.constants.base_values import base_values


def process_data(reservation):
    base_dataframe = pd.DataFrame(base_values, columns=['no_of_adults', 'no_of_children', 'no_of_weekend_nights',
                                                        'no_of_week_nights', 'type_of_meal_plan', 'required_car_parking_space',
                                                        'room_type_reserved', 'lead_time', 'arrival_year', 'arrival_month',
                                                        'arrival_date', 'market_segment_type', 'repeated_guest',
                                                        'no_of_previous_cancellations', 'no_of_previous_bookings_not_canceled',
                                                        'no_of_special_requests', 'booking_status'])

    attributes_array = np.array([
        reservation.no_of_adults,
        reservation.no_of_children,
        reservation.no_of_weekend_nights,
        reservation.no_of_week_nights,
        reservation.type_of_meal_plan,
        reservation.required_car_parking_space,
        reservation.room_type_reserved,
        reservation.lead_time,
        reservation.arrival_year,
        reservation.arrival_month,
        reservation.arrival_date,
        reservation.market_segment_type,
        reservation.repeated_guest,
        reservation.no_of_previous_cancellations,
        reservation.no_of_previous_bookings_not_canceled,
        reservation.no_of_special_requests,
        reservation.booking_status,
    ])

    new_row_df = pd.DataFrame(
        [attributes_array], columns=base_dataframe.columns)

    result_dataframe = pd.concat(
        [base_dataframe, new_row_df], ignore_index=True)
    result_dataframe = pd.get_dummies(result_dataframe, columns=[
                                      'type_of_meal_plan', 'room_type_reserved', 'market_segment_type', 'booking_status'])
    reservation_values = result_dataframe[-1:].to_csv(sep=",", header=False)
    reservation_values = reservation_values[2:]

    return reservation_values
