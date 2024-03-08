import datetime

from internal.account import Account
from internal.message import Message
from internal.booking import Booking
from internal.mate import Mate
from internal.customer import Customer
from internal.payment import Payment
from internal.transaction import Transaction
from internal.mate import Mate
from internal.review import Review
from internal.chat_room_manager import ChatRoomManeger
from internal.post import Post
from internal.message import Message
from models.mate import Date
from utils.auth import register
from dependencies import create_token

class Controller:
    def __init__(self) -> None:
        self.__account_list: list = []
        self.__booking_list: list = []
        self.__post_list: list = []
        self.__chat_room_list: list[ChatRoomManeger] = []

    def add_instance(self):
        account_1 = register("ganThepro", "1234", "customer")
        print("account_1_token :", create_token(str(account_1['id']), "customer"))
        account_2 = register("ganThepro2", "1234", "mate")
        print("account_2_token :", create_token(str(account_2['id']), "mate"))
        chat_room = self.add_chat_room(account_1['id'], account_2['id'])
        print("chat_room: ", chat_room.get_chat_room_details())

        account_3 = register("pawit", "1234", "customer")
        account_4 = register("yok", "1234", "mate")
        self.add_chat_room(account_1['id'], account_4['id'])
        self.add_chat_room(account_3['id'], account_2['id'])
        self.add_chat_room(account_3['id'], account_4['id'])

        account_5 = register("yok2", "1234", "mate")
        account_6 = register("yok3", "1234", "mate")
        account_7 = register("yok4", "1234", "mate")

        # self.add_customer("test1", "test1")
        # self.add_mate("test2", "test2")
        # self.add_customer("test3", "test3")
        # self.add_mate("test4", "test4")
        # self.add_customer("test5", "test5")
        # self.add_mate("test6", "test6")
        # self.add_customer("test7", "test7")
        # self.add_mate("test8", "test8")
        # my_acc = self.search_account_by_username("ganThepro")

        # mate_acc = self.add_mate("Mate1", "1234")
        # mate_acc2 = self.add_mate("Mate2", "1234")
        # # print("mate_acc: ", mate_acc.id)
        # # print("mate_acc: ", mate_acc2.id)
        # mate_acc.add_availablility(datetime.date(2024, 3, 4), "I'm available")
        # mate_acc2.add_availablility(datetime.date(2024, 3, 4), "I'm available")
        # self.add_booking(my_acc, mate_acc, Date(year=2024, month=3, day=4))

        # self.add_chat_room(Chat(my_acc, mate_acc))
        # self.add_chat_room(Chat(my_acc, mate_acc2))
    def get_chat_by_owner_pair(self, owner1, owner2):
        if not (isinstance(owner1, Account) and isinstance(owner2, Account)):
            raise TypeError("owner1, owner2 must be Account instances")
        for chat in self.__chat_room_list:
            chat_owner1 = chat.get_owner1()
            chat_owner2 = chat.get_owner2()
            if((owner1 in [chat_owner1, chat_owner2]) and (owner2 in [chat_owner1, chat_owner2]) and (chat_owner1 != chat_owner2)):
                return chat
        return None

    def get_chat_list(self):
        return self.__chat_room_list
    
    def get_chat_history_by_id(self, chat_room_id: str) -> list | None:
        chat_room = self.search_chat_room_by_id(chat_room_id)
        if chat_room:
            return chat_room.message_list
        return None
        
    def add_chat_room(self, account_1_id: str, account_2_id: str) -> ChatRoomManeger | None:
        account_1: Account = self.search_account_by_id(account_1_id)
        account_2: Account = self.search_account_by_id(account_2_id)
        if not (isinstance(account_1, Account) and isinstance(account_2, Account)):
            return None
        chat_room: ChatRoomManeger = ChatRoomManeger(account_1, account_2)
        self.__chat_room_list.append(chat_room)
        return chat_room

    def search_account_by_id(self, id: str):
        for acc in self.__account_list:
            if(id == str(acc.id)):
                return acc
        return None

    def talk(self, sender_id: str, receiver_id: str, text: str):
        sender = self.search_account_by_id(sender_id)
        receiver = self.search_account_by_id(receiver_id)
        chat = self.get_chat_by_owner_pair(sender, receiver)
        if(chat != None):
            timestamp = datetime.datetime.now()
            msg = chat.save_chat_log(Message(sender, text, timestamp))
            return msg
        return None
    
    def delete_message(self, sender_id: str, receiver_id: str, message_id: str):
        sender = self.search_account_by_id(sender_id)
        receiver = self.search_account_by_id(receiver_id)
        chat = self.get_chat_by_owner_pair(sender, receiver)
        if(chat != None):
            msg_list = chat.delete_message(message_id)
            return msg_list
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
                "sender_username" : sender_name,
                "message_id" : msg.id,
                "text" : msg.get_text(),
                "timestamp" : msg.get_timestamp(),
                "is_edit": msg.is_edit
            }
            all_chat_data.append(chat_data)
        return all_chat_data   

    def get_receiver_chat_room_detail(self, sender_acc):
        detail = []
        if not (isinstance(sender_acc, Account)):
            raise TypeError("receiver_acc must be Account instances")
        for chat in self.__chat_room_list:
            chat_owner1 = chat.account_1
            chat_owner2 = chat.account_2
            if((sender_acc in [chat_owner1, chat_owner2])):
                if(len(chat.message_list) >= 1):
                    latest_chat = chat.message_list[-1]
                    detail.append({
                        'account_detail' : chat_owner1.get_account_details() if sender_acc != chat_owner1 else chat_owner2.get_account_details(),
                        'latest_timestamp' : latest_chat.get_message_details()['timestamp'],
                        'latest_text' : latest_chat.get_message_details()['text'],
                        'chat_room_id': str(chat.id)
                    })
                else:
                    detail.append({
                        'account_detail' : chat_owner1.get_account_details() if sender_acc != chat_owner1 else chat_owner2.get_account_details(),
                        'latest_timestamp' : "",
                        'latest_text' : "",
                        'chat_room_id': str(chat.id)
                    })
        
        return detail

    def retrieve_chat_room(self, sender_id):
        sender_acc = self.search_account_by_id(sender_id)
        if not (isinstance(sender_acc, Account)):
            raise TypeError("No Acc found")
        detail = self.get_receiver_chat_room_detail(sender_acc)
        return detail
    
    def delete_chat_room(self, sender_id, receiver_id) -> list | None:
        sender_acc = self.search_account_by_id(sender_id)
        receiver_acc = self.search_account_by_id(receiver_id)
        if not (isinstance(sender_acc, Account) and isinstance(receiver_acc, Account)):
            raise "No Acc found"
        chat = self.get_chat_by_owner_pair(sender_acc, receiver_acc)
        if chat:
            self.__chat_room_list = [c for c in self.__chat_room_list if c != chat]
            return self.get_receiver_chat_room_detail(sender_acc)
        else:
            return None

    @property
    def account_list(self) -> list:
        return self.__account_list
    @property
    def booking_list(self) -> list:
        return self.__booking_list

    def add_customer(self, username: str, password: str) -> Customer:
        existed_account: Account = self.search_account_by_username(username)
        if existed_account != None:
            return None
        customer: Customer = Customer(username, password)
        self.__account_list.append(customer)
        return customer

    def add_mate(self, username: str, password: str) -> Mate:
        existed_account: Account = self.search_account_by_username(username)
        if existed_account != None:
            return None
        mate: Mate = Mate(username, password)
        self.__account_list.append(mate)
        return mate

    def search_account_by_username(self, username: str) -> Account | None:
        for account in self.__account_list:
            if account.username == username:
                return account
        return None

    def search_mate_by_display_name_similar(self, display_name: str) -> list | None:
        account_list = []
        for account in self.get_mates():
            if display_name in account.display_name:
                account_list.append(account)
        if(len(account_list)):
            return account_list
        return None
    
    def search_booking_by_id(self, booking_id: str) -> Booking | None:
        for booking in self.__booking_list:
            if str(booking.id) == booking_id:
                return booking
        return None
    
    def search_customer_by_id(self, customer_id: str) -> Account | None:
        for account in self.get_customers():
            if str(account.id) == customer_id:
                return account
        return None

    def search_mate_by_id(self, mate_id: str) -> Mate | None:
        for account in self.get_mates():
            if str(account.id) == mate_id:
                return account
        return None
    
    def search_mate_by_condition(self, name: str, location: str, gender: str, age: int) -> Mate | None:
        account_list = self.search_mate_by_display_name_similar(name)
        if len(account_list):
            return account_list
        return None
    
    def search_chat_room_by_id(self, chat_room_id: str) -> ChatRoomManeger | None:
        for chat_room in self.__chat_room_list:
            if str(chat_room.id) == chat_room_id:
                return chat_room
        return None

    def pay(self, booking_id: str) -> Transaction:
        booking: Booking = self.search_booking_by_id(booking_id)
        if booking == None:
            return None
        customer: Customer = self.search_customer_by_id(str(booking.customer.id))
        
        # customer : Customer = self.validate_customer(booking.customer)
        # todo : make validate function to all instances
        
        if customer == None:
            return None
        mate: Mate = self.search_mate_by_id(str(booking.mate.id))
        if mate == None:
            return None
        payment: Payment = booking.payment
        payment.pay(customer, mate)
        self.add_chat_room(customer, mate)
        transaction: Transaction = Transaction(customer, mate, payment.amount)
        customer.add_transaction(transaction)
        mate.add_transaction(transaction)
        return transaction
    
    def get_account_by_name(self, name: str) -> Account | None:
        for account in self.__account_list:
            if name in account.name:
                return account
        return None

    def get_mates(self) -> list:
        mate_list = []
        for account in self.__account_list:
            if isinstance(account, Mate):
                mate_list.append(account)
        return mate_list

    def get_customers(self) -> list:
        customer_list = []
        for account in self.__account_list:
            if isinstance(account, Customer):
                customer_list.append(account)
        return customer_list
    
    
    def add_booking(self, customer: Customer, mate: Mate, date: Date) -> Booking | None:
        booked_customer: Account = mate.book(customer, date.year, date.month, date.day)
        if booked_customer == None:
            return None
        booking: Booking = Booking(customer, mate, Payment(mate.amount))
        self.__booking_list.append(booking)
        return booking
    
    def get_booking(self, customer: Customer) -> list[Booking]:
        booking_list = []
        for booking in self.__booking_list:
            if booking.customer == customer:
                booking_list.append(booking)
        return booking_list

    def delete_booking(self, booking_id: str) -> Booking | None:
        booking: Booking = self.search_booking_by_id(booking_id)
        if booking:
            self.__booking_list.remove(booking)
            return booking
        else:
            return None

    def add_post(self, description: str, picture: str) -> Post | None:
        if not isinstance(description, str) or not isinstance(picture, str):
            return None
        post = Post(description, picture)
        self.__post_list.append(Post)
        return post
    
    def edit_display_name(self, customer_id: str, new_username: str):
        customer_acc: Account = self.search_account_by_id(customer_id)
        customer_acc.display_name = new_username
        return customer_acc
    
    def edit_pic_url(self, customer_id: str, new_pic_url: str):
        customer_acc: Account = self.search_account_by_id(customer_id)
        customer_acc.pic_url = new_pic_url
        return customer_acc
    
    def get_leaderboard(self):
        mate_list = self.get_mates()
        sorted_mates = sorted(mate_list, key=lambda mate: (mate.get_average_review_star(), mate.get_review_amount(), mate.timestamp), reverse=True)
        return sorted_mates[:10]







