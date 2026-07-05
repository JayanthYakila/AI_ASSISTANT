import os
import subprocess


def open_notepad():
    subprocess.Popen("notepad")


def open_calculator():
    subprocess.Popen("calc")


def open_explorer():
    subprocess.Popen("explorer")


def open_vscode():
    vscode = os.path.expandvars(
        r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"
    )

    if os.path.exists(vscode):
        subprocess.Popen(vscode)
        return True

    return False


def shutdown():
    os.system("shutdown /s /t 1")


def restart():
    os.system("shutdown /r /t 1")