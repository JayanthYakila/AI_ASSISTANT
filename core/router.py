from llm.chat import ask_llm

from memory.memory import remember, recall

from tools.browser import (
    google,
    youtube,
    chatgpt,
    github,
    gmail,
    linkedin,
    google_search,
    youtube_search,
    github_search,
    linkedin_search,
)

from tools.system import (
    open_notepad,
    open_calculator,
    open_explorer,
    open_vscode,
)


def process_command(command):

    command = command.lower()

    # ---------------- Memory ---------------- #

    if command.startswith("remember"):

        try:
            text = command.replace("remember", "").strip()

            key, value = text.split(" is ", 1)

            key = key.strip()
            value = value.strip()

            remember(key, value)

            return f"I'll remember that {key} is {value}."

        except:
            return "Please say it like: Remember name is Jayanth."

    elif command.startswith("what is"):

        key = command.replace("what is", "").strip()

        value = recall(key)

        if value:
            return f"{key} is {value}."

        else:
            return "I don't know that yet."

    # ---------------- Browser Search ---------------- #

    elif command.startswith("search google for"):

        query = command.replace("search google for", "").strip()

        google_search(query)

        return f"Searching Google for {query}."

    elif command.startswith("search youtube for"):

        query = command.replace("search youtube for", "").strip()

        youtube_search(query)

        return f"Searching YouTube for {query}."

    elif command.startswith("search github for"):

        query = command.replace("search github for", "").strip()

        github_search(query)

        return f"Searching GitHub for {query}."

    elif command.startswith("search linkedin for"):

        query = command.replace("search linkedin for", "").strip()

        linkedin_search(query)

        return f"Searching LinkedIn for {query}."

    # ---------------- Browser ---------------- #

    elif "google" in command:
        google()
        return "Opening Google."

    elif "youtube" in command:
        youtube()
        return "Opening YouTube."

    elif "chatgpt" in command:
        chatgpt()
        return "Opening ChatGPT."

    elif "github" in command:
        github()
        return "Opening GitHub."

    elif "gmail" in command:
        gmail()
        return "Opening Gmail."

    elif "linkedin" in command:
        linkedin()
        return "Opening LinkedIn."

    # ---------------- System ---------------- #

    elif "notepad" in command:
        open_notepad()
        return "Opening Notepad."

    elif "calculator" in command:
        open_calculator()
        return "Opening Calculator."

    elif "explorer" in command:
        open_explorer()
        return "Opening File Explorer."

    elif "vs code" in command:
        open_vscode()
        return "Opening Visual Studio Code."

    # ---------------- AI ---------------- #

    else:
        return ask_llm(command)