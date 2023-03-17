from booking_infos import BookingInfos

def test_origin_city():
    # Ensure the origin city is set correctly
    booking = BookingInfos(or_city='Rennes')
    assert booking.or_city == "Rennes"

def test_destination_city():
    # Ensure the destination city is set correctly
    booking = BookingInfos(dst_city='Paris')
    assert booking.dst_city == "Paris"

def test_budget():
    # Ensure the budget is set correctly
    booking = BookingInfos(budget=800)
    assert booking.budget == 800