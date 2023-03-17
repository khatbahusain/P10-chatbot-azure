class BookingInfos:
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
