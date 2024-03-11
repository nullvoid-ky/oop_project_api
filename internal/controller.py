from typing import Tuple, Union
import datetime

from internal.account import UserAccount, Account
from internal.admin import Admin
from internal.log import Log
from internal.booking import Booking
from internal.mate import Mate
from internal.customer import Customer
from internal.payment import Payment
from internal.transaction import Transaction
from internal.chat_room_manager import ChatRoomManeger
from utils.auth import register
from dependencies import create_token
from internal.post import Post
from models.mate import Date
import datetime

class Controller:
    def __init__(self) -> None:
        self.__account_list: list = []
        self.__booking_list: list = []
        self.__post_list: list = []
        self.__chat_room_list: list[ChatRoomManeger] = []
        self.__admin = None
        self.__log_list: list = []

    def add_instance(self):
        temp_detail_1 = register("temporaryaccount1", "qwer", "mate", "female")
        temp_detail_2 = register("temporaryaccount2", "qwer", "mate", "male")
        temp_detail_3 = register("temporaryaccount3", "qwer", "mate", "male")
        temp_detail_4 = register("temporaryaccount4", "qwer", "mate", "male")
        temp_detail_5 = register("temporaryaccount5", "qwer", "mate", "female")
        temp_detail_6 = register("temporaryaccount6", "qwer", "mate", "female")
        print(("temp_1"), create_token(str(temp_detail_1['id']), "mate"))
        print(("temp_2"), create_token(str(temp_detail_2['id']), "mate"))
        print(("temp_3"), create_token(str(temp_detail_3['id']), "mate"))
        print(("temp_4"), create_token(str(temp_detail_4['id']), "mate"))
        print(("temp_5"), create_token(str(temp_detail_5['id']), "mate"))
        print(("temp_6"), create_token(str(temp_detail_6['id']), "mate"))
        tmp1 = self.search_account_by_id(temp_detail_1['id'])
        tmp2 = self.search_account_by_id(temp_detail_2['id'])
        tmp3 = self.search_account_by_id(temp_detail_3['id'])
        tmp4 = self.search_account_by_id(temp_detail_4['id'])
        tmp5 = self.search_account_by_id(temp_detail_5['id'])
        tmp6 = self.search_account_by_id(temp_detail_6['id'])
        tmp_list =[tmp1, tmp2, tmp3, tmp4, tmp5, tmp6]
        for tmp in tmp_list:
            tmp.pic_url = "https://i1.sndcdn.com/artworks-ubBjVp0Z50ZykDdG-lU7NWg-t500x500.jpg"
            tmp.amount = 1234
            tmp.price = 3000
        tmp1.display_name = "Edok"
        tmp2.display_name = "Thong"
        tmp3.display_name = "Eson-Teen"
        tmp4.display_name = "GanGayOnline"
        for i in range(5):
            tmp5.add_availability(datetime.date(2024, 3, 4+i), f"I'm available laew {i}")

        account_1_details = register("ganThepro", "1234", "customer", "male")
        print("account_1_token :", create_token(str(account_1_details['id']), "customer"))
        account_2_details = register("ganThepro2", "1234", "mate", "female")
        print("account_2_token :", create_token(str(account_2_details['id']), "mate"))
        account_1: Customer = self.search_account_by_id(account_1_details['id'])
        account_2: Mate = self.search_account_by_id(account_2_details['id'])
        account_2.pic_url = "https://i1.sndcdn.com/artworks-ubBjVp0Z50ZykDdG-lU7NWg-t500x500.jpg"
        account_1.amount = 0    
        account_2.price = 1000
        chat_room = self.add_chat_room(account_1, account_2)
        print("chat_room: ", chat_room.get_chat_room_details())
        account_2.add_availability(datetime.date(2024, 3, 4), "I'm available")
        # print(account_2.availability_list)
        account_2.add_review_mate(account_1, "good", 4)
        self.add_booking(account_1, account_2, Date(year=2024, month=3, day=4))
        # booking, transaction = self.add_booking(account_1, account_2, Date(year=2024, month=3, day=4))
        # print("booking: ", booking.id)    
        # self.pay(str(booking.id))
        # print(account_2.get_success_booking(self.__booking_list))
        print(account_2.id)

        account_4_details: Mate = register("ganThepro3", "1234", "mate", "female")
        account_5_details: Mate = register("ganThepro4", "1234", "mate", "male")
        account_6_details: Mate = register("yok", "1234", "mate", "male")
        account_4: Mate = self.search_account_by_id(account_4_details['id'])
        account_5: Mate = self.search_account_by_id(account_5_details['id'])
        account_6: Mate = self.search_account_by_id(account_6_details['id'])

        account_2.add_review_mate(account_1, "So Good", 5)
        account_2.add_review_mate(account_1, "So Good", 4)
        account_4.add_review_mate(account_1, "So Good", 4)
        account_5.add_review_mate(account_1, "So Good", 2)
        account_6.add_review_mate(account_1, "So Good", 5)

        chat_room = self.add_chat_room(account_1, account_4)
        chat_room = self.add_chat_room(account_2, account_4)

        self.add_post(account_2, "Hello kra", "")
        self.add_post(account_4, "luv you na", "")
        self.add_post(account_5, "Hello krub", "")

        self.create_admin()
        print(f'Admin ID : {self.__admin.id}')
        print(f'Admin username : {self.__admin._username}')
        print(f'Admin password : {self.__admin._password}')
        self.edit_display_name(tmp6, "Narak")
        print(self.__log_list)
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
        # self.add_booking(my_acc, mate_acc, Date(year=2024, month=3, day=4))

        # self.add_chat_room(Chat(my_acc, mate_acc))
        # self.add_chat_room(Chat(my_acc, mate_acc2))
    def get_chat_by_owner_pair(self, owner1, owner2):
        if not (isinstance(owner1, UserAccount) and isinstance(owner2, UserAccount)):
            raise TypeError("owner1, owner2 must be UserAccount instances")
        for chat in self.__chat_room_list:
            chat_owner1 = chat.get_owner1()
            chat_owner2 = chat.get_owner2()
            if((owner1 in [chat_owner1, chat_owner2]) and (owner2 in [chat_owner1, chat_owner2]) and (chat_owner1 != chat_owner2)):
                return chat
        return None
    
    def get_chat_list(self, account: UserAccount) -> list | None:
        chat_list = []
        for chat in self.__chat_room_list:
            if chat.account_1 == account or chat.account_2 == account:
                chat_list.append(chat.get_chat_room_details())
        if len(chat_list) == 0:
            return None
        return chat_list
    
    def get_chat_history_by_id(self, chat_room_id: str) -> list | None:
        chat_room = self.search_chat_room_by_id(chat_room_id)
        if chat_room:
            return chat_room.message_list
        return None
        
    def add_chat_room(self, account_1: UserAccount, account_2: UserAccount) -> ChatRoomManeger | None:
        if not (isinstance(account_1, UserAccount) and isinstance(account_2, UserAccount)):
            return None
        chat_room: ChatRoomManeger = ChatRoomManeger(account_1, account_2)
        for chat in self.__chat_room_list:
            if str(chat.account_1.id) == str(chat_room.account_1.id) and str(chat.account_2.id) == str(chat_room.account_2.id):
                print("add chat: " ,chat.get_chat_room_details(), chat_room.get_chat_room_details())
                return None
        self.__chat_room_list.append(chat_room)
        return chat_room

    def search_account_by_id(self, id: str) -> UserAccount | None:
        for acc in self.__account_list:
            if(acc.validate_account_id(str(id))):
                return acc
        if isinstance(self.__admin, Admin):
            if(self.__admin.validate_account_id(str(id))):
                return self.__admin
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
        if not (isinstance(sender_acc, UserAccount) and isinstance(receiver_acc, UserAccount)):
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

    def get_receiver_chat_room_detail(self, sender_acc: UserAccount) -> list:
        detail = []
        if not (isinstance(sender_acc, UserAccount)):
            raise TypeError("receiver_acc must be UserAccount instances")
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
        if not (isinstance(sender_acc, UserAccount)):
            raise TypeError("No Acc found")
        detail = self.get_receiver_chat_room_detail(sender_acc)
        return detail
    
    def delete_chat_room(self, sender_id, receiver_id) -> list | None:
        sender_acc = self.search_account_by_id(sender_id)
        receiver_acc = self.search_account_by_id(receiver_id)
        if not (isinstance(sender_acc, UserAccount) and isinstance(receiver_acc, UserAccount)):
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

    def add_customer(self, username: str, password: str, gender: str, location: str) -> Customer:
        existed_account: UserAccount = self.search_account_by_username(username)
        if existed_account != None:
            return None
        customer: Customer = Customer(username, password, gender, location)
        self.__account_list.append(customer)
        return customer

    def add_mate(self, username: str, password: str, gender: str, location: str) -> Mate:
        existed_account: UserAccount = self.search_account_by_username(username)
        if existed_account != None:
            return None
        mate: Mate = Mate(username, password, gender, location)
        self.__account_list.append(mate)
        return mate

    def search_account_by_username(self, username: str) -> Mate | Customer | Admin | None:
        for account in self.__account_list:
            if account.username == username:
                return account
        if isinstance(self.__admin, Admin):
            if username == "admin":
                return self.__admin
        return None

    def search_mate_by_display_name_similar(self, display_name: str) -> list | None:
        account_list = []
        for account in self.get_mates():
            if display_name.lower() in account.display_name.lower():
                account_list.append(account)
        if(len(account_list)):
            return account_list
        return None
    
    def get_mate_by_username(self, username: str) -> list[Mate] | None:
        mate_list = []
        for account in self.get_mates():
            if username == account.username:
                mate_list.append(account)
        if len(mate_list) == 0:
            return None
        return mate_list
    
    def get_mate_by_gender(self, gender: str) -> list[Mate] | None:
        mate_list = []
        for mate in self.get_mates():
            if mate.gender == gender:
                mate_list.append(mate)
        if len(mate_list) == 0:
            return None
        return mate_list
    
    def get_mate_by_age(self, age: str) -> list[Mate] | None:
        mate_list = []
        for mate in self.get_mates():
            if mate.age >= age:
                mate_list.append(mate)
        if len(mate_list) == 0:
            return None
        return mate_list
    
    def get_mate_by_avalibility(self) -> list[Mate] | None:
        mate_list = []
        for mate in self.get_mates():
            if len(mate.availability_list) > 0:
                mate_list.append(mate)
        if len(mate_list) == 0:
            return None
        return mate_list
    
    def get_mate_by_location(self, location) -> list[Mate] | None:
        mate_list = []
        for mate in self.get_mates():
            if location.lower() in mate.location.lower():
                mate_list.append(mate)
        if len(mate_list) == 0:
            return None
        return mate_list
    
    def search_booking_by_id(self, booking_id: str) -> Booking | None:
        for booking in self.__booking_list:
            if str(booking.id) == booking_id:
                return booking
        return None
    
    def search_customer_by_id(self, customer_id: str) -> UserAccount | None:
        for account in self.get_customers():
            if str(account.id) == customer_id:
                return account
        return None

    def search_mate_by_id(self, mate_id: str) -> Mate | None:
        for account in self.get_mates():
            if str(account.id) == mate_id:
                return account
        return None
    
    def search_mate_by_condition(self, name: str, location: str, gender_list: list, age: int, availability: bool) -> Mate | None:
        account_list_by_name = self.search_mate_by_display_name_similar(name) if self.search_mate_by_display_name_similar(name) != None else []
        account_list_by_availability = self.get_mate_by_avalibility() if self.get_mate_by_avalibility() != None and availability else self.get_mates()
        account_list_by_location = self.get_mate_by_location(location) if self.get_mate_by_location(location) != None else []
        account_list_by_age = self.get_mate_by_age(age) if self.get_mate_by_age(age) != None else []
        account_list_by_gender_male = []
        account_list_by_gender_female = []
        account_list_by_gender = []
        if("male" in gender_list):
            account_list_by_gender_male = self.get_mate_by_gender("male") if self.get_mate_by_gender("male") != None else []

        if("female" in gender_list):
            account_list_by_gender_female = self.get_mate_by_gender("female") if self.get_mate_by_gender("female") != None else []
        account_list_by_gender = set(account_list_by_gender_male).union(account_list_by_gender_female)

        common_accounts = set(account_list_by_name)  # Convert the first list to a set
        common_accounts.intersection_update(account_list_by_availability)
        common_accounts.intersection_update(account_list_by_location)
        common_accounts.intersection_update(account_list_by_gender)
        common_accounts.intersection_update(account_list_by_age)
        common_accounts = list(common_accounts)

        print("account_list_by_name: ", account_list_by_name)
        print("account_list_by_availability: ", account_list_by_availability)
        print("account_list_by_location: ", account_list_by_location)
        print("account_list_by_gender: ", account_list_by_gender)
        print("account_list_by_age: ", account_list_by_age)
        print("common_accounts: ", common_accounts)

        if common_accounts!=None:
            return common_accounts
        return None
    
    def search_chat_room_by_id(self, chat_room_id: str) -> ChatRoomManeger | None:
        for chat_room in self.__chat_room_list:
            if str(chat_room.id) == chat_room_id:
                return chat_room
        return None

    def pay(self, booking_id: str) -> Transaction:
        booking: Booking = self.search_booking_by_id(booking_id)
        customer: Customer = self.search_customer_by_id(str(booking.customer.id))
        if customer == None:
            return None
        mate: Mate = self.search_mate_by_id(str(booking.mate.id))
        if mate == None or customer == None or booking == None:
            return None
        payment: Payment = booking.payment
        if payment.pay(customer, mate) == False:
            return None
        if self.add_chat_room(customer, mate) == None:
            return None
        transaction: Transaction = Transaction(customer, mate, payment.amount)
        customer.add_transaction(transaction)
        mate.add_transaction(transaction)
        booking.status = "Success"
        return transaction
    
    def get_account_by_name(self, name: str) -> UserAccount | None:
        for account in self.__account_list:
            if name in account.name:
                return account
        return None

    def get_mates(self) -> list[Mate]:
        mate_list = []
        for account in self.__account_list:
            if isinstance(account, Mate):
                mate_list.append(account)
        return mate_list

    def get_customers(self) -> list[Customer]:
        customer_list = []
        for account in self.__account_list:
            if isinstance(account, Customer):
                customer_list.append(account)
        return customer_list
    
    def add_booking(self, customer: Customer, mate: Mate, date: Date) -> Tuple[Booking, Transaction] | None:
        pledge_payment: Payment = Payment(mate.price / 2)
        if pledge_payment.pay(customer, mate) == False:
            return None
        booked_customer: Account = mate.book(date.year, date.month, date.day)
        if booked_customer == None:
            return None
        pledge_transaction: Transaction = Transaction(customer, mate, pledge_payment.amount)   
        customer.add_transaction(pledge_transaction)
        mate.add_transaction(pledge_transaction)
        booking: Booking = Booking(customer, mate, datetime.date(date.year, date.month, date.day), pledge_payment)
        self.__booking_list.append(booking)
        return booking, pledge_transaction
    
    def get_booking(self, account: Account) -> list[Booking]:
        if not isinstance(account, Account):
            return []
        booking_list = []
        for booking in self.__booking_list:
            if booking.customer == account or booking.mate == account:
                booking_list.append(booking)
        return booking_list

    def delete_booking(self, booking: Booking, account: UserAccount) -> Union[Tuple[Booking, Transaction], Booking, None]:
        transaction: Transaction = None
        if not isinstance(booking, Booking):
            return None
        if not isinstance(account, Account):
            return None

        if isinstance(account, Mate):
            if booking.payment.pay(account, booking.customer) == False:
                return None
            transaction: Transaction = Transaction(account, booking.customer, booking.payment.amount)
        if isinstance(booking, Booking):
            booking.mate.booked_customer = None
            booking.status = "Failed"
            booking.mate.add_availability(datetime.date(booking.book_date.year, booking.book_date.month, booking.book_date.day), "I'm available")
            if transaction:
                return booking, transaction
            return booking
        return None
    
    def get_all_transaction(self):
        transaction = []
        for account in self.account_list:
            transaction = transaction + account.transaction_list
        return transaction
    
    def get_all_booking(self):
        booking_list = []
        for booking in self.__booking_list:
            booking_list.append(booking)
        return booking_list

    def add_post(self, writer: Mate, description: str, picture: str) -> Post | None:
        if not isinstance(description, str) or not isinstance(picture, str) or not isinstance(writer, Mate):
            self.add_log(False, writer, "add_post" ,"No Item", writer, "Instance Error")
            return None
        post = Post(writer, description, picture)
        self.__post_list.append(post)
        self.add_log(True, writer, "add_post" ,post, writer, "Added Post")
        return post
    
    def get_post(self):
        if len(self.__post_list) == 0:
            return None
        return self.__post_list

    def edit_display_name(self, account: Account, new_display_name: str) -> Account:
        if not isinstance(account, Account) or not isinstance(new_display_name, str):
            self.add_log(False, account, "edit_display_name" , "No Item", account, "Instance Error")
            return None
        self.add_log(True, account, "edit_display_name" ,new_display_name, account, "Edited name")
        account.display_name = new_display_name
        return account
    
    def edit_pic_url(self, account: UserAccount, new_pic_url: str) -> UserAccount:
        if not isinstance(account, Account) or not isinstance(new_pic_url, str):
            self.add_log(False, account, "edit_pic_url" ,"No Item", account, "Instance Error")
            return None
        self.add_log(True, account, "edit_pic_url" ,new_pic_url, account, "Edited Pic")
        account.pic_url = new_pic_url
        return account

    def edit_money(self, account: UserAccount, new_money: str) -> UserAccount:
        if not isinstance(account, Account) or not isinstance(new_money, str):
            self.add_log(False, account, "edit_money" ,"No Item", account, "instanec Error")
            return None
        self.add_log(True, account, "edit_money" ,new_money, account, "Adjusted Money")
        account.amount = new_money
        return account
    
    def edit_age(self, account: Account, new_age: int) -> Account:
        if not isinstance(account, Account) or not(isinstance(new_age,int)):
            self.add_log(False, account, "edit_age" ,"No Item", account, "Instance Error")
        account.age = new_age
        self.add_log(True, account, "edit_age" ,new_age, account, "Edited Age")
        return account

    def edit_location(self, account: Account, new_location: str) -> Account:
        if not isinstance(account, Account) or not(isinstance(new_location,str)):
            self.add_log(False, account, "edit_location" ,"No Item", account, "Instance Error")
        account.location = new_location
        self.add_log(True, account, "edit_location" ,new_location, account, "Edited Location")
        return account
    
    # def edit_gender(self, account: UserAccount, new_money: str) -> UserAccount:
    #     if not isinstance(account, Account) or not isinstance(new_money, str):
    #         self.add_log(False, account, "edit_money" ,"", None)
    #         return None
    #     self.add_log(True, account, "edit_money" ,new_money, None)
    #     account.amount = new_money
    #     return account
    
    def get_leaderboard(self) -> list[Mate]:
        mate_list = self.get_mates()
        for mate in mate_list:
            print(mate.get_average_review_star(), mate.get_review_amount(), mate.timestamp)
        sorted_mates = sorted(mate_list, key=lambda mate: (mate.get_average_review_star(), mate.get_review_amount(), mate.timestamp), reverse=True)
        return sorted_mates[:10]
    
    def add_log(self, success, actor, action, item, target, msg) -> None:
        self.__log_list.append(Log(success, actor, action, item, target, msg))

    def create_admin(self) -> Admin | None:
        if isinstance(self.__admin, Admin):
            return None
        self.__admin = Admin()
        return self.__admin
    
    def get_log(self) -> list | None:
        if self.__log_list == []:
            return None
        return self.__log_list
    
    def get_admin(self) -> Admin:
        return self.__admin
    
    @property
    def log_list(self):
        return self.__log_list