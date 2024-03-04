import datetime

class Availablility:
    def __init__(self, date: datetime, detail: str):
        self.__date = date
        self.__detail = detail
    @property
    def date(self) -> datetime:
        return self.__date
    @property
    def detail(self) -> str:
        return self.__detail

    def check_available(self, year: int, month: int, day: int) -> bool:
        return str(datetime.date(year, month, day)) == str(self.__date)