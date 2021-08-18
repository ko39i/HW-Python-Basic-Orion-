import socket
import threading
import re
import argparse
import json



def read_sock():
    while True:
        data = sock.recv(1024).decode('utf-8')
        try:
            user_nickname = re.search("\[(.*)\]", data).group(0)
        except AttributeError:
            user_nickname = ''
        if user_nickname not in blocked_users:
            print(data)
        else:
            message = "@" + recipient + ", " + " you blocked by this user"
            sock.sendto(('[' + alias + '] ' + message).encode('utf-8'), server)



server = ('127.0.0.28', 3279)
f = open("users.json", "r")
users_data = f.readline()
alias = input("Your username: ")
f.close()
for args in users_data:
    if users_data == alias:
        print("Error")
    else:
        continue
f = open("users.json", "w")
# users_data.append(alias)
f.write(alias)
f.close()


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 0))
sock.sendto(("[" + alias + "] Connect to server").encode('utf-8'), server)
blocked_users = []

potik = threading.Thread(target=read_sock)
potik.start()

# def chek_user():
#     while True:
#         data, address = sock.recvfrom(1024)
#         nickname = re.search("@(.*),", data.decode('utf-8'))
#         nickname = nickname.group(0)
#         nickname = list(nickname)
#         del nickname[0]
#         del nickname[-1]
#         nickname = "".join(nickname)
#         for address in clients:
#             if clients[address] == "[" + nickname + "]":
#                 msg = "nickname is unloked"
#                 sock.sendto((msq).data, server)
#                 return alias
#             else:
#                 break

while True:
    print('1. Send message to group chat')
    print('2. Send private message')
    print('3. Block user')
    try:
        menu_choose = int(input(':'))
    except ValueError:
        continue
    if menu_choose == 1:
        message = input("Your message: ")
        sock.sendto(('[' + alias + '] ' + message).encode('utf-8'), server)
    elif menu_choose == 2:
        recipient = input('Recipient(Nickname): ')
        message = input("Your message: ")
        message = "@" + recipient + ", " + message
        sock.sendto(('[' + alias + '] ' + message).encode('utf-8'), server)
    elif menu_choose == 3:
        recipient = input('Which user you want to block ? (Nickname): ')
        blocked_users.append("[" + recipient + "]")
        print("User " + recipient + " blocked!")