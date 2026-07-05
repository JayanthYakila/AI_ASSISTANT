from speech.listen import listen
from core.router import process_command


def start():

    print("\nAssistant Started\n")

    while True:

        command = listen()

        if not command:
            continue

        print(f"\nYou: {command}")

        if command.lower() == "exit":
            break

        response = process_command(command)

        print(f"\nAssistant: {response}")