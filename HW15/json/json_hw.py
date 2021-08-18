import argparse
import json

parser = argparse.ArgumentParser()

parser.add_argument("--username", help="Your user username")
parser.add_argument("--mail", help="Your mail")
args = parser.parse_args()
user_dict = {}

if args.username:
    user_dict['username'] = args.username

if args.mail:
    user_dict['mail'] = args.mail

user_file = open('users.json', 'r')
users_data = json.loads(user_file.readline())
user_file.close()
for args in users_data:
    if user_dict == args:
        print("Error")
    else:
        continue

users_data.append(user_dict)
user_file = open('users.json', 'w')
user_file.write(json.dumps(users_data))
user_file.close()


