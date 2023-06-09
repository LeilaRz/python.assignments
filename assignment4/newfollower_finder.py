
from getpass import getpass
import instaloader


username = input("Username: ")
password = getpass("Password: ")

L = instaloader.Instaloader()
L.login(username, password)
print("you successfuly logged in")

profile = instaloader.Profile.from_username(L.context, "leylarazeghi")

f = open("assignment4/newfollower.txt", "r")
old_followers = []
for line in f:
    old_followers.append(line.strip())
f.close()

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower.username)

for new_follower in new_followers:
    if new_follower not in old_followers:
        print(new_follower)

f = open("newfollower.txt", "w")
for new_follower in new_followers:
    f.write(new_follower + "\n")
f.close()