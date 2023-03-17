import unittest

class BookingDetails:
    def __init__(
        self,
        or_city: str = None,
        dst_city: str = None,
        str_date: str = None,
        end_date: str = None,
        budget: str = None,
    ):
        
        self.or_city: str = or_city
        self.dst_city: str = dst_city
        self.str_date: str = str_date
        self.end_date: str = end_date
        self.budget: str = budget

class TestAPI(unittest.TestCase):
    def test_origin_city(self):
        # Ensure the origin city is set correctly
        booking = BookingDetails(or_city='Rennes')
        assert booking.or_city == "Rennes"

    def test_destination_city(self):
        # Ensure the destination city is set correctly
        booking = BookingDetails(dst_city='Paris')
        assert booking.dst_city == "Paris"

    def test_budget(self):
        # Ensure the budget is set correctly
        booking = BookingDetails(budget=800)
        assert booking.budget == 800
    
    
    

if __name__ == '__main__':
    unittest.main()
