# implementation of stack in python using list and pop() list method.
import time
import bcrypt
import datetime

# thisislist = []
#
# thisislist.append(1)
# thisislist.append('thisisstring')
# thisislist.append(3)
#
# print(thisislist)
#
# thisislist.pop()
#
# print(thisislist)
# print(thisislist.pop())
# print(thisislist)
#
# start = time.time()
# for i in range(540650):
#     a = 1
# print(time.time() - start)

# password = b'thisispassword'
# a = bcrypt.gensalt()
# hashed = bcrypt.hashpw(password, a)
#
# print(hashed)
# print(hashed.decode('utf8'))
#
# string = str(hashed[2:-1])
#
# if bcrypt.checkpw(password, hashed):
#     print("logged in")
# else:
#     print("wrong")
#
# print(a)
#
# def kas():
#     a = 1
#     return
#
# print(type(kas()))

# import json
# import urllib.request
# import re
#
# a = urllib.request.urlopen('https://api.themoviedb.org/3/search/movie?api_key=15d2ea6d0dc1d476efbca3eba2b9bbfb&query=%22onward%22&callback=?')
# a = a.read().decode().replace("?", '').replace("(", '').replace(")", '').replace('false', 'False').replace("true", 'True').replace("null", "None")
# a = eval(a)
# with open ('moviedata.json', 'w', encoding='utf-8') as f:
#     json.dump(a, f, ensure_ascii=False, indent=4)
# # overview = re.findall(r'"overview":"[A-Za-z0-9]+\."', a)
# # print(overview)
# print(a)
# print(type(a))

a = datetime.date(2021, 11, 4)
a = a.strftime("%d %B %Y")
print(a)

