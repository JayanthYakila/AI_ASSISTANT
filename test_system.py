from tools.system import *

print("1. Notepad")
print("2. Calculator")
print("3. Explorer")
print("4. VS Code")

choice = input("Choose: ")

if choice == "1":
    open_notepad()

elif choice == "2":
    open_calculator()

elif choice == "3":
    open_explorer()

elif choice == "4":
    if not open_vscode():
        print("VS Code not found.")