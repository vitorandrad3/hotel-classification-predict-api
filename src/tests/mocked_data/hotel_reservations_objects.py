from src.models.hotel_reservation import HotelReservationData


reservation_data_test1 = HotelReservationData(
    no_of_adults=2,
    no_of_children=0,
    no_of_weekend_nights=1,
    no_of_week_nights=2,
    type_of_meal_plan="Meal Plan 1",
    required_car_parking_space=0,
    room_type_reserved="Room_Type 1",
    lead_time=224,
    arrival_year=2017,
    arrival_month=10,
    arrival_date=2,
    market_segment_type="Offline",
    repeated_guest=0,
    no_of_previous_cancellations=0,
    no_of_previous_bookings_not_canceled=0,
    no_of_special_requests=0,
    booking_status="Not_Canceled"
)

reservation_data_test2 = HotelReservationData(
    no_of_adults=3,
    no_of_children=2,
    no_of_weekend_nights=4,
    no_of_week_nights=2,
    type_of_meal_plan="Meal Plan 1",
    required_car_parking_space=2,
    room_type_reserved="Room_Type 1",
    lead_time=224,
    arrival_year=2017,
    arrival_month=10,
    arrival_date=2,
    market_segment_type="Offline",
    repeated_guest=0,
    no_of_previous_cancellations=0,
    no_of_previous_bookings_not_canceled=0,
    no_of_special_requests=0,
    booking_status="Not_Canceled"
)

reservation_data_test3 = HotelReservationData(
    no_of_adults=3,
    no_of_children=0,
    no_of_weekend_nights=2,
    no_of_week_nights=6,
    type_of_meal_plan="Meal Plan 1",
    required_car_parking_space=0,
    room_type_reserved="Room_Type 4",
    lead_time=85,
    arrival_year=2018,
    arrival_month=8,
    arrival_date=3,
    market_segment_type="Online",
    repeated_guest=0,
    no_of_previous_cancellations=0,
    no_of_previous_bookings_not_canceled=0,
    no_of_special_requests=1,
    booking_status="Not_Canceled"
)
