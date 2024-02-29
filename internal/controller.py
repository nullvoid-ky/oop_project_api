from internal.account import Account
from internal.message import Message
from internal.chat import Chat
import datetime
from internal.booking import Booking
from internal.mate import Mate
from internal.customer import Customer
from internal.payment import Payment
from internal.transaction import Transaction

class Controller:
    def __init__(self) -> None:
        self.__account_list: list = []
        self.__booking_list: list = []
        self.__chat_list = []

    def get_chat_list(self):
        return self.__chat_list
    
    def add_chat_room(self, chat):
        if not (isinstance(chat, Chat)):
            raise TypeError("chat must be Chat instances")

        self.__chat_list.append(chat)

    # def add_account_instance(self, acc):
    #     self.__account_list.append(acc)
    #     print("\nAdd acc success : len ", len(self.__account_list))
    
    def search_account_by_id(self, id):
        # print("\n\n")
        # print(len(self.__account_list))
        for acc in self.__account_list:
            print(acc.get_account_details())
            if(id == str(acc.id)):
                return acc
        return None

    def get_chat_by_owner_pair(self, owner1, owner2):
        if not (isinstance(owner1, Account) and isinstance(owner2, Account)):
            raise TypeError("owner1, owner2 must be Account instances")
        
        for chat in self.__chat_list:
            chat_owner1 = chat.get_owner1()
            chat_owner2 = chat.get_owner2()

            if((owner1 in [chat_owner1, chat_owner2]) and (owner2 in [chat_owner1, chat_owner2]) and (chat_owner1 != chat_owner2)):
                return chat
        
        return None

    def talk(self, sender_id, receiver_id, text):
        # print(sender_id, receiver_id)
        sender = self.search_account_by_id(sender_id)
        receiver = self.search_account_by_id(receiver_id)
        # print(type(sender), type(receiver))
        chat = self.get_chat_by_owner_pair(sender, receiver)

        if(chat != None):
            timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            chat.save_chat_log(Message(sender, receiver, text, timestamp))
            return chat
        return None

    def retrieve_chat_log(self, sender_id, receiver_id):
        sender_acc = self.search_account_by_id(sender_id)
        receiver_acc = self.search_account_by_id(receiver_id)

        if not (isinstance(sender_acc, Account) and isinstance(receiver_acc, Account)):
            raise "No Acc found"
        
        chat = self.get_chat_by_owner_pair(sender_acc, receiver_acc)
        message_list = chat.get_message_list()

        all_chat_data = []
        for msg in message_list:
            sender_name = msg.get_sender_name()
            chat_data = {
                sender_name : {
                    "text" : msg.get_text(),
                    "timestamp" : msg.get_timestamp()
                }
            }
            all_chat_data.append(chat_data)

        return all_chat_data   

    def get_receiver_chat_room_detail(self, sender_acc):
        detail = []
        if not (isinstance(sender_acc, Account)):
            raise TypeError("receiver_acc must be Account instances")
        
        for chat in self.__chat_list:
            chat_owner1 = chat.get_owner1()
            chat_owner2 = chat.get_owner2()
            
            if((sender_acc in [chat_owner1, chat_owner2]) and len(chat.get_message_list()) >= 1):
                latest_chat = chat.get_message_list()[-1]
                detail.append({
                        'account_detail' : latest_chat.get_sender_account().get_account_details(),
                        'latest_timestamp' : latest_chat.get_timestamp(),
                        'latest_text' : latest_chat.get_text(),
                })
        
        return detail
    

    def retrieve_chat_room(self, sender_id):
        sender_acc = self.search_account_by_id(sender_id)

        if not (isinstance(sender_acc, Account)):
            raise "No Acc found"
        detail = self.get_receiver_chat_room_detail(sender_acc)

        return detail
    @property
    def account_list(self) -> list:
        return self.__account_list
    @property
    def booking_list(self) -> list:
        return self.__booking_list

    async def add_instance(self):
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
        customer_acc = await self.add_customer("Kan", "1234")
        print(customer_acc.id)
        mate_acc = await self.add_mate("Gan", "1234")
        print(mate_acc.id)
        mate_acc2 = await self.add_mate("Nan", "1234")
        print(mate_acc2.id)

        self.add_chat_room(Chat(customer_acc, mate_acc))
        self.add_chat_room(Chat(customer_acc, mate_acc2))

    async def add_customer(self, username: str, password: bytes) -> Customer:
        existed_account: Account = await self.search_account_by_username(username)
        if existed_account != None:
            return None
        customer: Customer = Customer(username, password)
        self.__account_list.append(customer)
        return customer

    async def add_mate(self, username: str, password: bytes) -> Mate:
        existed_account: Account = await self.search_account_by_username(username)
        if existed_account != None:
            return None
        mate: Mate = Mate(username, password)
        self.__account_list.append(mate)
        return mate

    def add_booking(self, customer: Customer, mate: Mate, amount: int) -> Booking:
        booking: Booking = Booking(customer, mate, Payment(amount, False))
        self.__booking_list.append(booking)
        return booking

    async def search_account_by_username(self, username: str) -> Account | None:
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
    
    async def search_booking(self, booking_id: str) -> dict:
        for booking in self.__booking_list:
            if str(booking.id) == booking_id:
                return booking.get_booking_detail()

    async def add_payment(self, booking_id: str) -> dict:
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
        self.add_chat_room(Chat(customer, mate))
        transaction: Transaction = Transaction(customer, mate, payment.amount)
        return transaction.get_transaction_details()