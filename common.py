import datetime
import os
import yaml
import openai


######################### Global variables #########################
GLOBAL_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
GLOBAL_CONFIG = {}
GLOBAL_FINE_TUNE_MODEL = {}
GLOBAL_MESSAGE_NOT_SUPPORTED_YET = "Not supported yet!"


######################### Tools #########################


def print_time_stamp(input_str: str):
    separator = "*" * 40
    print(f"""{separator}  {input_str} {str(datetime.datetime.now())}  {separator}""")


def print_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())


def convert_timestamp_to_datetime(timestamp_str: str) -> str:
    # Convert the timestamp to a datetime object
    date = datetime.datetime.fromtimestamp(timestamp_str)

    # Format the date as a string
    return date.strftime(GLOBAL_DATETIME_FORMAT)


def get_model_suffix() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")


######################### Config #########################
def load_config():
    try:
        global GLOBAL_CONFIG

        file_path = r"config.example.yaml"
        ignore_path = r"config.yaml"
        if os.path.exists(ignore_path):
            file_path = ignore_path

        with open(file_path, "r") as file:
            GLOBAL_CONFIG = yaml.safe_load(file)
    except Exception as e:
        x = str(e)
        print("Error: ", x)
