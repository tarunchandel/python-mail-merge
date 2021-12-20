NAMES_FILE_PATH = "Input/Names/invited_names.txt"
STARTING_LETTER_PATH = "Input/Letters/starting_letter.txt"
INVITES_PATH = "Output/ReadyToSend"

with open(NAMES_FILE_PATH, mode="r") as file:
    names = file.readlines()

with open(STARTING_LETTER_PATH, mode="r") as file:
    letter_text = file.read()

for name in names:
    name = name.strip("\n")
    invite_text = letter_text.replace("[name]", name)
    with open(f"{INVITES_PATH}/letter_for_{name}.txt", mode="w") as file:
        file.write(invite_text)