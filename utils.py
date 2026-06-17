import os


def create_output_folder():

    if not os.path.exists("outputs"):
        os.makedirs("outputs")


def save_output(filename, content):

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)