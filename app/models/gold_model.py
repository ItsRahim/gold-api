from dataclasses import dataclass
from datetime import datetime


@dataclass
class Gold:
    price: float
    date_time: datetime
    source: str

    @property
    def formatted_datetime(self):
        return self.date_time.strftime("%Y-%m-%d %H:%M:%S")
