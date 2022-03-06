import vk_api, time, colorama
from colorama import Fore
import os
import sys
from vk_api.longpoll import VkLongPoll, VkEventType

banner = """

██╗░░░██╗██╗░░██╗███╗░░░███╗░██████╗░██████╗░██████╗░
██║░░░██║██║░██╔╝████╗░████║██╔════╝██╔════╝██╔════╝░
╚██╗░██╔╝█████═╝░██╔████╔██║╚█████╗░╚█████╗░██║░░██╗░
░╚████╔╝░██╔═██╗░██║╚██╔╝██║░╚═══██╗░╚═══██╗██║░░╚██╗
░░╚██╔╝░░██║░╚██╗██║░╚═╝░██║██████╔╝██████╔╝╚██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░╚═════╝░░╚═════╝░
"""


print(Fore.CYAN + banner)

token = input("Введите токен: ")
users = input("Введите id: ")
vk_session = vk_api.VkApi(token=token)
api = vk_session.get_api()
def main():
    try:
        chats = input('Кол-во бесед: ')
        spot = 0
        while int(spot) < int(chats):
            api.messages.createChat(user_ids=users, title="VKMSSG")
            spot += 1
            time.sleep(15)
        print(spot)
    except Exception as er:
        print(er)


main()

