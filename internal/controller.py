from internal.account import Account
from internal.message import Message
import datetime
import bcrypt

class Controller:
    def __init__(self) -> None:
        self.__account_list: list = []
        self.__booking_list: list = []
        self.__chat_list = []

    def get_chat_list(self):
        return self.__chat_list
    
    def add_chat_room(self, chat):
        self.__chat_list.append(chat)

    def add_account_instance(self, acc):
        self.__account_list.append(acc)
        print("\nAdd acc success : len ", len(self.__account_list))
    
    def search_account_by_id(self, id):
        print("\n\n")
        print(len(self.__account_list))
        for acc in self.__account_list:
            print(acc.get_account_details())
            if(id == str(acc.id)):
                return acc
        return None

    def get_chat_by_owner_pair(self, owner1, owner2):
        if not (isinstance(owner1, Account) and isinstance(owner2, Account)):
            print(type(owner1), type(owner2))
            raise TypeError("owner1, owner2 must be Account instances")
        
        for chat in self.__chat_list:
            chat_owner1 = chat.get_owner1()
            chat_owner2 = chat.get_owner2()

            if((owner1 in [chat_owner1, chat_owner2]) and (owner2 in [chat_owner1, chat_owner2]) and (chat_owner1 != chat_owner2)):
                return chat
        
        return None

    def talk(self, sender_id, receiver_id, text):
        print(sender_id, receiver_id)
        sender = self.search_account_by_id(sender_id)
        receiver = self.search_account_by_id(receiver_id)
        print(type(sender), type(receiver))
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
            
            if((sender_acc in [chat_owner1, chat_owner2])):
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
    
    def add_account(self, username: str, password: str) -> Account:
        account: Account = Account(username, password)
        self.__account_list.append(account)
        return account

    async def get_account_by_username(self, username: str) -> Account | None:
        for account in self.__account_list:
            if account.username == username:
                return account
        return None
    
    class Auth:
        def __init__(self, username: str, password: str) -> None:
            self.__user = username
            self.__password = password

        async def register(self) -> dict | None:
            account: Account = await self.get_account_by_username(self.__user)
            if account == None:
                # return None
                hashed_password = bcrypt.hashpw(self.__password.encode('utf-8'), bcrypt.gensalt())
                new_account: Account = self.add_account(self.__user, str(hashed_password))
                return new_account.get_account_details()
            return None

        async def login(self):
            account: Account = await self.get_account_by_username(self.__user)
            if account == None:
                return None
            if bcrypt.checkpw(self.__password.encode('utf-8'), account.password):
                return account.get_account_details()
            return None