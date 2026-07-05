from tools.browser import *

print("1 Google")
print("2 YouTube")
print("3 ChatGPT")
print("4 GitHub")
print("5 Gmail")
print("6 LinkedIn")

choice = input("Choose: ")

if choice == "1":
    google()

elif choice == "2":
    youtube()

elif choice == "3":
    chatgpt()

elif choice == "4":
    github()

elif choice == "5":
    gmail()

elif choice == "6":
    linkedin()