from internal.account import Account
from internal.booking import Booking
from internal.mate import Mate
from internal.customer import Customer
from internal.payment import Payment
from internal.transaction import Transaction

class Controller:
    def __init__(self) -> None:
        self.__account_list: list = []
        self.__booking_list: list = []
    @property
    def account_list(self) -> list:
        return self.__account_list
    @property
    def booking_list(self) -> list:
        return self.__booking_list

    async def create_instance(self):
        await self.add_customer("test1", "test1")
        await self.add_mate("test2", "test2")
        await self.add_customer("test3", "test3")
        await self.add_mate("test4", "test4")
        await self.add_customer("test5", "test5")
        await self.add_mate("test6", "test6")
        await self.add_customer("test7", "test7")
        await self.add_mate("test8", "test8")
        self.add_booking(self.account_list[0], self.account_list[1], 100)
        self.add_booking(self.account_list[2], self.account_list[3], 200)
        self.add_booking(self.account_list[4], self.account_list[5], 300)
        self.add_booking(self.account_list[6], self.account_list[7], 400)

    async def add_customer(self, username: str, password: bytes) -> Customer:
        existed_account: Account = await self.get_account_by_username(username)
        if existed_account != None:
            return None
        customer: Customer = Customer(username, password)
        self.__account_list.append(customer)
        await self.create_instance()
        return customer

    async def add_mate(self, username: str, password: str) -> Mate:
        existed_account: Account = await self.get_account_by_username(username)
        if existed_account != None:
            return None
        mate: Mate = Mate(username, password)
        self.__account_list.append(mate)
        return mate

    def add_booking(self, customer: Customer, mate: Mate, amount: int) -> Booking:
        booking: Booking = Booking(customer, mate, Payment(amount))
        self.__booking_list.append(booking)
        return booking

    async def get_account_by_username(self, username: str) -> Account | None:
        for account in self.__account_list:
            if account.username == username:
                return account
        return None
    
    async def search_booking_by_id(self, booking_id: str) -> Booking | None:
        for booking in self.__booking_list:
            if str(booking.id) == booking_id:
                return booking
        return None
    
    async def search_customer_by_id(self, customer_id: str) -> Account | None:
        for account in self.__account_list:
            if str(account.id) == customer_id:
                return account
        return None

    async def search_mate_by_id(self, mate_id: str) -> Mate | None:
        for account in self.__account_list:
            if str(account.id) == mate_id:
                return account
        return None

    async def create_payment(self, booking_id: str) -> dict:
        booking: Booking = await self.search_booking_by_id(booking_id)
        if booking == None:
            return "Booking not found"
        customer: Customer = await self.search_customer_by_id(str(booking.customer.id))
        if customer == None:
            return "Customer not found"
        mate: Mate = await self.search_mate_by_id(str(booking.mate.id))
        if mate == None:
            return "Mate not found"
        payment: Payment = booking.payment
        payment.pay(customer, mate)
        transaction: Transaction = Transaction(customer, mate, payment.amount)
        return transaction.get_transaction_details()