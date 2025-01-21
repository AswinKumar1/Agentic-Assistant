import os

NOTES_DIR = "notes/"

if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

def save_note(content, filename):
    with open(os.path.join(NOTES_DIR, filename), "w") as file:
        file.write(content)

def list_notes():
    return os.listdir(NOTES_DIR)

def read_note(filename):
    with open(os.path.join(NOTES_DIR, filename), "r") as file:
        return file.read()
