

from rent_a_mate import *
web = Controller()
web.add_user( User("Tamtikorn", 19, 0))
web.add_user( User("Nakul", 19, 0))
web.add_user( User("Thanatchaya", 19, 1))
web.add_user( User("TajIsWomen", 19, 1))
web.add_user( User("NattapasIsWomen", 20, 1))

gan_user = web.search_user_by_name("Tamtikorn")
porche_user = web.search_user_by_name("Nakul")
mook_user = web.search_user_by_name("Thanatchaya")
taj_user = web.search_user_by_name("TajIsWomen")
nat_user = web.search_user_by_name("NattapasIsWomen")

web.sign_up_as_customer(gan_user, "ganxd123", "Ab12345")
web.sign_up_as_customer(porche_user, "porchenarak", "Cd23456")
web.sign_up_as_mate(mook_user, "mamoruuko","25032005")
web.sign_up_as_mate(taj_user, "tajnarak", "password")
web.sign_up_as_mate(nat_user, "transparent", "qwerty123")

gan_account = web.login("ganxd123", "Ab12345")
porche_account = web.login("porchenarak", "Cd23456")
mook_account = web.login("mamoruuko", "25032005")
taj_account = web.login("tajnarak", "password")
nat_account = web.login("transparent", "qwerty123")

local_account_list = [gan_account,porche_account,mook_account,taj_account,nat_account]

mook_account.add_display_name("Mookjung")
taj_account.add_display_name("Tajung_kawaii")

mook_account.add_available(Available("ECC", "19:00", "21:00", "19 Feb 2024"))
mook_account.add_available(Available("ECC", "19:00", "21:00", "18 Feb 2024"))
mook_account.add_available(Available("ECC", "19:00", "21:00", "22 Feb 2024"))
mook_account.add_available(Available("ECC", "19:00", "21:00", "23 Feb 2024"))

taj_account.add_available(Available("Dormitory", "19:00", "21:00", "22 Feb 2024"))
taj_account.add_available(Available("Dormitory", "19:00", "21:00", "15 Feb 2024"))
taj_account.add_available(Available("Dormitory", "19:00", "21:00", "28 Feb 2024"))

mate_by_name = web.search_mate_by_name("jung")
print(Controller.change_name_to_json(mate_by_name))