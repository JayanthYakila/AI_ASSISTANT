import os
import subprocess
from urllib.parse import quote_plus


BRAVE = os.path.expandvars(
    r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\Application\brave.exe"
)


def open_url(url):

    if os.path.exists(BRAVE):
        subprocess.Popen([BRAVE, url])
        return True

    return False


# ---------------- Open Websites ---------------- #

def google():
    return open_url("https://www.google.com")


def youtube():
    return open_url("https://www.youtube.com")


def chatgpt():
    return open_url("https://chatgpt.com")


def github():
    return open_url("https://github.com")


def gmail():
    return open_url("https://mail.google.com")


def linkedin():
    return open_url("https://www.linkedin.com")


# ---------------- Search Websites ---------------- #

def google_search(query):
    url = f"https://www.google.com/search?q={quote_plus(query)}"
    return open_url(url)


def youtube_search(query):
    url = f"https://www.youtube.com/results?search_query={quote_plus(query)}"
    return open_url(url)


def github_search(query):
    url = f"https://github.com/search?q={quote_plus(query)}"
    return open_url(url)


def linkedin_search(query):
    url = f"https://www.linkedin.com/search/results/all/?keywords={quote_plus(query)}"
    return open_url(url)